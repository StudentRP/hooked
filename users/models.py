from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """New model that extends the User model by a one-to-one relationship adding a profile pic field"""
    user = models.OneToOneField(User, on_delete=models.CASCADE) # 121 relationship with a user, user is the current logged in user.
    image = models.ImageField(default='default.jpg', upload_to='profile_pics') # default pic and where images are to be uploaded
    # can add any number of fields that have the above relationship

    def __str__(self):
        return f'{self.user.username} profile'
