from decimal import Decimal
import os
import stripe

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from stripe import StripeClient

from .models import Order


# Configure Stripe for webhook
stripe.api_key = settings.STRIPE_SECRET_KEY


def server_price(type_, size):
    base = {"logo": 30, "poster": 40, "icon": 20}[type_]
    mult = {"S": 1.0, "M": 1.5, "L": 2.0}[size]
    return Decimal(base * mult).quantize(Decimal("0.01"))


@login_required
def create_order(request):
    if request.method == "POST":
        type_ = request.POST.get("type")
        size = request.POST.get("size")
        desc = request.POST.get("description", "").strip()
        price = server_price(type_, size)

        order = Order.objects.create(
            user=request.user,
            type=type_,
            size=size,
            description=desc,
            price=price,
            paid=False,
        )

        client = StripeClient(settings.STRIPE_SECRET_KEY)

        success_url = (
            request.build_absolute_uri(reverse("payment_success"))
            + "?session_id={CHECKOUT_SESSION_ID}"
        )
        cancel_url = request.build_absolute_uri(reverse("create_order"))

        session = client.v1.checkout.sessions.create(
            mode="payment",
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "product_data": {
                            "name": f"{type_.title()} ({size})"
                        },
                        "unit_amount": int(price * 100),
                    },
                    "quantity": 1,
                }
            ],
            success_url=success_url,
            cancel_url=cancel_url,
            metadata={"order_id": str(order.id)},
        )
        return redirect(session.url)

    return render(
        request,
        "orders/order_form.html",
        {"stripe_public_key": settings.STRIPE_PUBLIC_KEY},
    )


@login_required
def payment_success(request):
    session_id = request.GET.get("session_id")
    order = None
    if session_id:
        try:
            session = stripe.checkout.sessions.retrieve(session_id)
            oid = (session.get("metadata") or {}).get("order_id")
            if oid:
                order = Order.objects.filter(id=oid, user=request.user).first()
        except Exception:
            pass
    return render(request, "orders/payment_success.html", {"order": order})


@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by("-id")
    return render(request, "orders/my_orders.html", {"orders": orders})


# Webhook to mark orders as paid after successful checkout
@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE", "")
    wh_secret = os.getenv("STRIPE_WEBHOOK_SECRET", "")

    if not wh_secret:
        return HttpResponseBadRequest("Missing webhook secret")

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, wh_secret)
    except ValueError:
        return HttpResponseBadRequest("Invalid payload")
    except stripe.error.SignatureVerificationError:
        return HttpResponseBadRequest("Invalid signature")

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        order_id = (session.get("metadata") or {}).get("order_id")
        if order_id:
            try:
                o = Order.objects.get(id=order_id)
                o.paid = True
                o.save(update_fields=["paid"])
            except Order.DoesNotExist:
                pass

    return HttpResponse(status=200)
