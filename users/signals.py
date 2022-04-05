"""signals for adding default profile image.
Want to create a profile for each new user"""

from django.db.models.signals import post_save # want a post_save signal when a user is created
from django.contrib.auth.models import User # the sender
from django.dispatch import receiver # receives the signal
from .models import Profile


@receiver(post_save, sender=User) # when user is saved, send a signal that is received by this decorator, the
def create_profile(sender, instance, created, **kwargs): # receiver activates this function where post_save provides all the args bellow
    if created:
        Profile.objects.create(user=instance) # CRUD command create. created new profile from the user instance (new user).


"""So... the receiver is looking for a post_save signal from the User model. 
  When it gets this the function is activated and the args from the post_save are pushed to the function created profile.
  If created evals to true then a profile is created for the user instance (the new user) """


#saves the user profile to Profile
@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    instance.profile.save()

