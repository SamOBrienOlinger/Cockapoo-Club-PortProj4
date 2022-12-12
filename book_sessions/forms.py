from .models import booking
from django import forms
from django.forms import ModelForm
# from .models import Photo


# class BookingForm(forms.ModelForm):
class BookingForm(ModelForm):
    class Meta:
        model = booking
        fields = "__all__"
        # fields = ['Username', 'Pword 1', 'Pword 2']

# class PhotoForm(ModelForm):
#     class Meta:
#         model = Photo
