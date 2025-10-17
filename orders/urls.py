from django.urls import path
from . import views

urlpatterns = [
    path("", views.create_order, name="create_order"),
    path("success/", views.payment_success, name="payment_success"),
    path("my/", views.my_orders, name="my_orders"),
]
