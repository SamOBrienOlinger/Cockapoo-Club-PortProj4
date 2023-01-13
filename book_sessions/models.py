from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django import forms
# from django.conf import settings

# Create your models here.


# create a form for booking a training session


class booking(models.Model):
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
    # VACC_YES = 'Y'
    # VACC_NO = 'N'
    # VACC_CHOICES = [
    #     (VACC_YES, 'Yes, my dog is vaccinated'),
    #     (VACC_NO, 'No, my dog is not vaccinated'),
    # ]
    # Vaccination_Status = models.CharField(
    #     max_length=1,
    #     choices=VACC_CHOICES,
    #     default=VACC_NO,
    # )

    booking_date_time = models.DateTimeField(auto_now=False, blank=True)
    confirmed = models.BooleanField(default=True)


class home(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)


class booking_detail(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    # vaccinated_yes = models.IntegerField(blank=True, default=0)
    # confirmed = models.BooleanField(default=True)

    # VACC_YES = models.BooleanField(default=False),
    # confirmed = models.BooleanField(default=False)

    # session_type = models.DateTimeField(auto_now=True, blank=True)
    # confirmed = models.BooleanField(default=False)

    # first_name = forms.CharField(required=True, max_length=255)
    # last_name = forms.CharField(required=True, max_length=255)
    # email = forms.EmailField(required=True)
    # phone = forms.CharField(required=True, max_length=200)
    # address = forms.CharField(max_length=1000, widget=forms.Textarea())
    # date = models.DateField(default="YYYY-MM-DD")
    # time = models.TimeField(default="00:00")
    # user_name = models.CharField(max_length=250)
    # user_email = models.EmailField()

#     class Meta:
#         unique_together = [['session_type', 'booking_date_time']]


# def __str__(self):
#     return self.session_type


# class Photo(models.Model):
#     image = CloudinaryField('image')
#     name = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='images/', blank=True)


# class BookingForm(forms.ModelForm):
#     first_name = forms.CharField(required=True, max_length=255)
#     last_name = forms.CharField(required=True, max_length=255)
#     email = forms.EmailField(required=True)
#     phone = forms.CharField(required=True, max_length=200)
#     address = forms.CharField(max_length=1000, widget=forms.Textarea())

    # class Meta:
    #     unique_together = [['first_name', 'last_name']]

# class Meta:
#      = [['', '']]


# def __str__(self):
#     return self.first_name

# class book a time slot for a training session:
#    allow user to:
#        Choose time
#        Choose date

#    submit button
#    reschedule/update button
#    delete/cancel button
