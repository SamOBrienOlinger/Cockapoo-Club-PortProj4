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


# class DogProfile(models.Model):
#     owner_name = forms.CharField(required=True, max_length=255)
#     dog_name = forms.CharField(required=True, max_length=255)
#     dog_age = forms.CharField(required=True, max_length=200)


# class NewMember(models.Model):
#     title = models.CharField(max_length=200, unique=True)
#     slug = models.SlugField(max_length=200, unique=True)
#     first_name = forms.CharField(required=True, max_length=255)
#     last_name = forms.CharField(required=True, max_length=255)
#     email = forms.EmailField(required=True)
#     phone = forms.CharField(required=True, max_length=200)
#     address = forms.CharField(max_length=1000, widget=forms.Textarea())
#     email = forms.EmailField(required=True)


# class Photo(models.Model):
#     image = CloudinaryField('image')
#     name = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='images/', blank=True)


# class home(models.Model):
#     title = models.CharField(max_length=200, unique=True)
#     slug = models.SlugField(max_length=200, unique=True)


# class home(models.Model):
#     title = models.CharField(max_length=200, unique=True)
#     slug = models.SlugField(max_length=200, unique=True)


# class PersonalDataForm(forms.Form):
#     first_name = forms.CharField(required=True, max_length=255)
#     last_name = forms.CharField(required=True, max_length=255)
#     email = forms.EmailField(required=True)
#     phone = forms.CharField(required=True, max_length=200)
#     address = forms.CharField(max_length=1000, widget=forms.Textarea())
