from django.db import models


class Design(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="designs/")
    testimonial = models.TextField(blank=True)

    def __str__(self):
        return self.title
