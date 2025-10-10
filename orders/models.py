from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    TYPE_CHOICES = [
        ("logo", "Logo"),
        ("poster", "Poster"),
        ("icon", "Icon"),
    ]
    SIZE_CHOICES = [
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    size = models.CharField(max_length=1, choices=SIZE_CHOICES)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
    )  # server-calculated
    paid = models.BooleanField(default=False)
    status = models.CharField(
        max_length=20,
        default="Pending",
    )  # Pending/Completed
    design_file = models.FileField(
        upload_to="completed/",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.user.username} - {self.type} {self.size} "
            f"(${self.price})"
        )
