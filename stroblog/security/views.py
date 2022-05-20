from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib import messages # You need to import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username") # We get the username to pass it to the message.
            messages.success(request, f"Account created for user {username}. Now you can log in.") # The alert.
            return redirect(to="login")
    else:
        form = SignupForm()
    return render(request, "security/register.html", {"form": form})

@login_required
def profile(request):
    return render(request, "security/profile.html", {})
