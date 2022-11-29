from django.contrib import admin
from .models import booking, home, PersonalDataForm

# Register your models here.

admin.site.register(booking)

# @admin.site.register(booking)
# class booking(models.Model):
#     title = models.CharField(max_length=200, unique=True)
#     slug = models.SlugField(max_length=200, unique=True)


# @admin.site.register(home)
# class home(models.Model):
#     title = models.CharField(max_length=200, unique=True)
#     slug = models.SlugField(max_length=200, unique=True)


# @admin.site.register(PersonalDataForm)
# class PersonalDataForm(models.Model):
#     title = models.CharField(max_length=200, unique=True)
#     slug = models.SlugField(max_length=200, unique=True)
