from .models import booking
from django import forms


class BookingForm(forms.ModelForm):

    class Meta:
        model = booking()
        fields = ('body',)
