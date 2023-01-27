from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django import forms

# Create your models here.

class index(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)


def __str__(self):
    return self.first_name
