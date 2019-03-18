from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

# class UserModel(models.Model):
#     name = models.CharField(max_length=200, default="")
#     password = models.CharField(max_length=100, default="")
#     email = models.EmailField(default="")
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#
#     def __str__(self):
#         return self.name


class WikiEntryModel(models.Model):
    title = models.CharField(max_length=200, default="")
    text = models.TextField(max_length=2000, default="")
    createdDate = models.DateTimeField(default=datetime.now)
    updatedDate = models.DateTimeField(default=datetime.now)
    image = models.FileField(upload_to='images')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # keyword arguments , any argument passed into a function where you specify what you are passing.
        # its a redirect to each wikis page
        return reverse('WikiApp:eachWiki', args=[self.pk])

class RIEntryModel(models.Model):
    title = models.CharField(max_length=100, default="")
    text = models.TextField(max_length=1000, default="")
    createdDate = models.DateField(default=datetime.now)
    image = models.FileField(upload_to='images')
    wiki = models.ForeignKey(WikiEntryModel, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
