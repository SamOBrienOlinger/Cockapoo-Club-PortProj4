from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django import forms

# Create your models here.


class booking(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)


class home(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)


class BookingForm(forms.ModelForm):
    first_name = forms.CharField(required=True, max_length=255)
    last_name = forms.CharField(required=True, max_length=255)
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True, max_length=200)
    address = forms.CharField(max_length=1000, widget=forms.Textarea())

    # class Meta:
    #     unique_together = [['first_name', 'last_name']]

# class Meta:
#      = [['', '']]


def __str__(self):
    return self.first_name

# class book a time slot for a training session:

#    allow user to:
#    Choose time
#    Choose date

#    Submit button
#    Edit button
#    delete button

# class book(models.Model):
#   title = models.CharField(max_length=200, unique=True)
#   slug = models.SlugField(max_length=200, unique=True)
#   featured_image = CloudinaryField('image', default='placeholder')
