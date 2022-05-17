from django.urls import path
from . import views

urlpatterns = [
    path(route="", view=views.home, name="blog-home"),
    path(route="about-us/", view=views.about_us, name="blog-about-us")
]