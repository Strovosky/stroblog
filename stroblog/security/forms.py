from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailField, CharField


class SignupForm(UserCreationForm):
    first_name = CharField(max_length=100, required=True)
    last_name = CharField(max_length=120, required=True)
    email = EmailField(required=False)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", 'password1', 'password2', "email"]
