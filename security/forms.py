from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailField, CharField, ModelForm


class SignupForm(UserCreationForm):
    first_name = CharField(max_length=100, required=True)
    last_name = CharField(max_length=120, required=True)
    email = EmailField(required=False)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", 'password1', 'password2', "email"]


# On this one I will pass the fields I want the user to be able to update from the User model.
class UserUpdateForm(ModelForm):
    email = EmailField(required=False)

    class Meta:
        model = User
        fields = ["username", "email"]

# On this one I will pass the fields I want the user to be able to update from the Profile model.
class ProfileUpdateForm(ModelForm):
    # We leave this part blaked because we don't wanna add anything.
    class Meta:
        model = Profile
        fields = ["profile_pic"]
