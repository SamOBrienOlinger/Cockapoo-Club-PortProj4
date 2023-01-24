from .models import booking
from django import forms
from django.forms import ModelForm
# from .models import Photo
from django.contrib.admin import widgets


# class BookingForm(forms.ModelForm):
class BookingForm(ModelForm):
    booking_date_time = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
    )

    class Meta:
        model = booking
        # fields = "__all__"
        exclude = ["confirmed", "user"]
