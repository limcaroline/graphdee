from django.shortcuts import render
from .models import Design


def home(request):
    designs = Design.objects.all().order_by("-id")
    return render(request, "gallery/gallery.html", {"designs": designs})
