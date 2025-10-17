from django.urls import path
from . import views
from orders import views as order_views

urlpatterns = [
    path("", views.create_order, name="create_order"),
    path("success/", views.payment_success, name="payment_success"),
    path("my/", views.my_orders, name="my_orders"),
    path("stripe/webhook/", order_views.stripe_webhook, name="stripe_webhook"),

]
