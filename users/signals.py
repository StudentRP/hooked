"""signals for adding default profile image"""

from django.db.models.signals import post_save # want a post_save signal when a user is created
from django.contrib.auth.models import User # the sender
from django.dispatch import receiver # receives the signal
from .models import Profile







