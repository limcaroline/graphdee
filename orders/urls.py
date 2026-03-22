from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path("", views.create_order, name="create_order"),
    path("success/", views.payment_success, name="payment_success"),
    path("my/", views.my_orders, name="my_orders"),
    path('edit/<int:order_id>/', views.update_order, name='update_order'),
    path('delete/<int:order_id>/', views.delete_order, name='delete_order'),
]
