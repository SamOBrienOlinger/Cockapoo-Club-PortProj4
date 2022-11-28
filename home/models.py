from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django import forms

# Create your models here.
# STATUS = ((0, "Draft"), (1, "Published"))

class home(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)


class PersonalDataForm(forms.Form):
    first_name = forms.CharField(required=True, max_length=255)
    last_name = forms.CharField(required=True, max_length=255)
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True, max_length=200)
    address = forms.CharField(max_length=1000, widget=forms.Textarea())


# class signup():

# create username and password

#   enter/register details:
#     Username
#     Password
#     User/Owner name
#     Dog name
#     Dog age
#     Vaccinated (Y/N)
#     user submit button


# class signin:

#   authenticate username and password to login

#   bring user to booking page
