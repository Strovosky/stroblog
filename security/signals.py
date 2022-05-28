from django.db.models.signals import post_save
# This is a signal that is emitted once something is saved.

from django.contrib.auth.models import User
# This will be the sender of the signal (when a user is created.)

from django.dispatch import receiver
# The receiver

from .models import Profile
# Because we'll be creating a profile once we get the signal.


@receiver(signal=post_save, sender=User) # This means, when a user is saved, send this signal.
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# A function to save the profile everytime it is created.
@receiver(signal=post_save, sender=User) # This means, when a user is saved, send this signal.
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

