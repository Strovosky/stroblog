from django.shortcuts import render, redirect
from .forms import SignupForm, UserUpdateForm, ProfileUpdateForm
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
    if request.method == "POST":
        # To get the right form, we pass an instance of what it expects.
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        profile_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()
            username = user_update_form.cleaned_data.get("username")
            messages.success(request, f"Profile updated for user {username}.")
            
            # It is better to redirect here because of the POST - GET REDIRECT PATTERN.
            # That's the message that says (Do you want to submit info again?)
            return redirect(to="profile")
    else:
        # We pass the info of the user in the GET request becuase we want the fields...
        # ... with the info of the user already filled in.
        # If you don't want the fields already filled in, just leave the form blank.
        user_update_form = UserUpdateForm(instance=request.user)
        profile_update_form = ProfileUpdateForm(instance=request.user.profile)
    context = {"u_form": user_update_form, "p_form": profile_update_form}
    return render(request, "security/profile.html", context)
