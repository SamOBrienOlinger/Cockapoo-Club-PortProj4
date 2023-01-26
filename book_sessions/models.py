from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django import forms

# create model for booking a dog training session


class Booking(models.Model):
    ONE_ON_ONE = 'O'
    GROUP = 'G'
    SESSION_CHOICES_CHOICES = [
        (ONE_ON_ONE, 'One to One training session'),
        (GROUP, 'Group training session'),
    ]
    session_type = models.CharField(
        max_length=1,
        choices=SESSION_CHOICES_CHOICES,
        default=ONE_ON_ONE,
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    booking_date_time = models.DateTimeField(auto_now=False, blank=True)

    confirmed = models.BooleanField(default=False)


class Home(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)


class Booking_detail(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
