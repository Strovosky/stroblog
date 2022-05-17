from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': "Strovosky",
        'title': "The meaning of life.",
        "content": "I think life has no meaning.",
        "date_posted": "Feb 23rd"
    },
    {
        'author': "Gabriel",
        'title': "The importance of potato chips",
        "content": "They just taste super.",
        "date_posted": "Jan 27th"
    }
]

def home(request):
    content = {"posts": posts}
    return render(request, "blog/home.html", content)

def about_us(request):
    return render(request, "blog/about_us.html", {})
