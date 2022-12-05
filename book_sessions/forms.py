from .models import booking
from django import forms
from django.forms import ModelForm
# from .models import Photo


class BookingForm(forms.ModelForm):

    class Meta:
        model = booking
        fields = "__all__"


# class PhotoForm(ModelForm):
#     class Meta:
#         model = Photo
