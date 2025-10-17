from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path("", views.create_order, name="create_order"),
    path("success/", views.payment_success, name="payment_success"),
    path("my/", views.my_orders, name="my_orders"),
]
