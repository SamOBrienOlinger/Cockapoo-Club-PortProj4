from django.shortcuts import render, HttpResponse, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponse

from .forms import BookingForm
from . import models
# from cloudinary.forms import cl_init_js_callbacks
# from .models import Photo
# from .forms import PhotoForm
# from .models import Post
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.


@login_required
def booking(request):
    if request.method == "GET":
        booking_form = BookingForm()
        existing_bookings = []
        existing_bookings = models.booking.objects.filter(
            confirmed=True
        ).all()
        print(existing_bookings)
        return render(request, 'booking.html', context={"form": booking_form, "existing_bookings": existing_bookings})

    elif request.method == "POST":
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking = booking_form.save()
            messages.add_message(request, messages.SUCCESS, 'Booking successful.')
            return render(request, 'booking_detail.html', {"booking": booking})
        else:
            return render(request, 'booking.html', {"form": booking_form})


@login_required
def bookings(request):
    pass


@login_required
def update_booking(request, id):
    if request.method == "GET":
        existing_booking = get_object_or_404(models.booking, id=id)
        print(existing_booking)
        booking_form = BookingForm(instance=existing_booking)
        print(booking_form)
        return render(request, 'booking.html', context={"form": booking_form})

    elif request.method == "POST":
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.id = id
            booking.save()
            messages.add_message(request, messages.SUCCESS, 'Booking updated successfully.')
            return render(request, 'booking_detail.html', {"booking": booking})
        else:
            return render(request, 'booking.html', {"form": booking_form})



# @login_required
# # def update_booking(request):
# #     pass

# class update_booking(updateBooking):
#     model = booking(request)
#     template = 'booking_detail.html'
#     fields = '__all__'



@login_required
def delete_booking(request, id):
    existing_booking = get_object_or_404(models.booking, id=id)
    existing_booking.delete()

    return redirect("/booking")


def homepage(request):
    return render(request, "index.html")
