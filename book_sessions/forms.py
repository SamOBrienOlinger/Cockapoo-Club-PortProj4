from .models import booking
from django import forms
from django.forms import ModelForm
# from .models import Photo
from django.contrib.admin import widgets


# class BookingForm(forms.ModelForm):
class BookingForm(ModelForm):
    booking_date_time = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        # input_formats=['']
        # input_formats=['YYYY-MM-DD'],
        # input_formats=['%YY-%mm-%dd %H:%M']
        # input_formats=['%d/%m/%Y'],
        # widget=forms.DateTimeInput(attrs={
        #     'class': 'form-control datetimepicker-input',
        #     'data-target': '#datetimepicker1'
        # })
    )

    class Meta:
        model = booking
        # fields = "__all__"
        exclude = ["confirmed"]
        # fields = ['Username', 'Pword 1', 'Pword 2']

    # def __init__(self, *args, **kwargs):
    #      super(BookingForm, self).__init__(*args, **kwargs)
    #      self.fields['booking_date'].widget = widgets.AdminDateWidget()
    #      self.fields['booking_time'].widget = widgets.AdminTimeWidget()
        #  self.fields['mydatetime'].widget = widgets.AdminSplitDateTime()

# class PhotoForm(ModelForm):
#     class Meta:
#         model = Photo
