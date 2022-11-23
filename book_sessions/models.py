from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class booking(models.Model):
    # model = Booking
    template_name = "booking.html"
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

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
