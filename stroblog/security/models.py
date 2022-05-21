from django.db.models import Model, OneToOneField, CASCADE, DateField, ImageField, CharField

# First, import the User model, since this is the one we'll extend.
from django.contrib.auth.models import User

# Create your models here.

class Profile(Model):
    user = OneToOneField(to=User, on_delete=CASCADE)
    # Now you can add any other field you want to the user.
    birth_date = DateField(default=None, null=True, blank=True)
    gender = CharField(max_length=10, default=None, null=True, blank=True)
    # This is how you add a picture field. "profile_pics" is a directory that will be created.
    profile_pic = ImageField(default="default_pic.jpg", upload_to="profile_pics")

    def __str__(self) -> str:
        return f"{self.user.username} - Profile"
