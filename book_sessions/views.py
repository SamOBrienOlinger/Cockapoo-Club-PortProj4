from django.shortcuts import render, HttpResponse, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponse
from .forms import BookingForm
from book_sessions.models import (Booking, Home, Booking_detail)
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
        existing_bookings = Booking.objects.filter(
            confirmed=True, user=request.user
        ).all()
        print(existing_bookings)
        return render(request, 'booking.html', context={"form": booking_form, "existing_bookings": existing_bookings})

    elif request.method == "POST":
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            reservation = booking_form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            messages.add_message(request, messages.SUCCESS, 'Booking successful.')
            return render(request, 'booking_detail.html', {"booking": reservation})
        else:
            return render(request, 'booking.html', {"form": booking_form})


@login_required
def bookings(request):
    pass


@login_required
def update_booking(request, booking_id):
    existing_booking = get_object_or_404(Booking, pk=booking_id)
    if existing_booking.user != request.user:
        messages.error(request, 'this is not your booking')
        return redirect("index")

    if request.method == "POST":
        booking_form = BookingForm(request.POST, instance=existing_booking)
        if booking_form.is_valid():
            print(booking_form.cleaned_data)
            booking_form.save()
            messages.success(request, 'Booking updated successfully.')
            return redirect('all_bookings')
        else:
            return redirect('all_bookings')

    print(existing_booking)
    booking_form = BookingForm(instance=existing_booking)

    return render(request, 'booking.html', context={"form": booking_form})


@login_required
def delete_booking(request, booking_id):
    existing_bookings = get_object_or_404(Booking, pk=booking_id)
    if existing_bookings.user != request.user:
        messages.error(request, 'this is not your booking')
        return redirect("index")
    existing_bookings.delete()

    return redirect('all_bookings')


def homepage(request):
    return render(request, "index.html")
