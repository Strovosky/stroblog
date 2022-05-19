from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    user1_posts = User.objects.get(id=1).posts_set.all()
    return render(request, "blog/home.html", {"posts": user1_posts})

def about_us(request):
    return render(request, "blog/about_us.html", {})
