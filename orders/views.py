from decimal import Decimal

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from stripe import StripeClient

from .models import Order


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
    # MVP: Display success; (Stretch) verify via webhook and mark paid.
    return render(request, "orders/payment_success.html")


@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by("-id")
    return render(request, "orders/my_orders.html", {"orders": orders})
