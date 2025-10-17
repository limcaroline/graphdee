from django.urls import path
from .views import home, gallery_list

urlpatterns = [
    path("", home, name="home"),
    path("gallery/", gallery_list, name="gallery"),
]
