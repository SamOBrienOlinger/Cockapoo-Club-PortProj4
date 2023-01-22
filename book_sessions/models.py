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
    # confirmed = models.BooleanField(default=False)
    confirmed = models.BooleanField(default=False)


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

    # CREDIT:  - wierdlygoodcoder
    # URL: https://github.com/wierdlygoodcoder

# """Forms for the ``booking`` app."""
# from django import forms
# from django.conf import settings
# from django.contrib.auth import authenticate
# from django.contrib.auth.forms import AuthenticationForm
# from django.utils.translation import ugettext_lazy as _

# from .models import Booking, BookingStatus


# class BookingForm(forms.ModelForm):
#     def __init__(self, session=None, user=None, *args, **kwargs):
#         self.user = user
#         self.session = session
#         super(BookingForm, self).__init__(*args, **kwargs)
#         # fields that should remain blank / not required
#         keep_blank = [
#             'phone', 'notes', 'street2', 'title', 'user', 'session',
#             'date_from', 'date_until', 'special_request', 'time_period',
#             'time_unit', 'email', 'currency', 'total']
#         # set all fields except the keep_blank ones to be required, since they
#         # need to be blank=True on the model itself to allow creating Booking
#         # instances without data
#         for name, field in self.fields.items():
#             if name not in keep_blank:
#                 self.fields[name].required = True

#     def save(self, *args, **kwargs):
#         if not self.instance.pk:
#             self.instance.user = self.user
#             self.instance.session = self.session
#             status_object, created = BookingStatus.objects.get_or_create(
#                 slug=getattr(settings, 'BOOKING_STATUS_CREATED', 'pending'))
#             self.instance.booking_status = status_object
#         return super(BookingForm, self).save(*args, **kwargs)

#     class Meta:
#         model = Booking
#         fields = ('gender', 'title', 'forename', 'surname', 'nationality',
#                   'street1', 'street2', 'city', 'zip_code', 'country', 'phone',
#                   'special_request', 'date_from', 'date_until')


# class BookingIDAuthenticationForm(AuthenticationForm):
#     def __init__(self, *args, **kwargs):
#         super(BookingIDAuthenticationForm, self).__init__(*args, **kwargs)
#         self.fields['username'] = forms.CharField(
#             label=_("Email"), max_length=256)
#         self.fields['password'] = forms.CharField(
#             label=_("Booking ID"), max_length=100)

#     def clean_username(self):
#         """Prevent case-sensitive erros in email/username."""
#         return self.cleaned_data['username'].lower()

#     def clean(self):
#         email = self.cleaned_data.get('username')
#         booking_id = self.cleaned_data.get('password')

#         if email and booking_id:
#             self.user_cache = authenticate(username=email,
#                                            password=booking_id)
#             if self.user_cache is None:
#                 raise forms.ValidationError(_(
#                     'We cannot find a valid booking ID for this email'
#                     ' address.')
#                 )
#             elif not self.user_cache.is_active:
#                 raise forms.ValidationError(self.error_messages['inactive'])
#         self.check_for_test_cookie()
#         return self.cleaned_data
