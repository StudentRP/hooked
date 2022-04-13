from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse # for view redirection on CreateNews


class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     """required meth for url redirect after news creation."""
    #     return reverse("mb-news")


class Announcements(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title







"""
Note: when querying the shell User.objects.filter(username='rory') will return a query set object and NOT the 
actual person object ( if had more than one rory (if username was not unique.. Django default) this would show 
in the queryset as more than one object. However, select actual person object by either appending the .first() 
or .last() methods or using the .get(atrib='') method and finaly using the list index of the queryset.
 
"""