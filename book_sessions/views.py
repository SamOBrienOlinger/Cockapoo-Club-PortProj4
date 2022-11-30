from django.shortcuts import render
# HttpResponse, get_object_or_404, reverse
# from django.views import generic, View
from django.http import HttpResponse
from .models import booking
from .forms import BookingForm
# from .models import Post

# Create your views here.


def booking(request):
    if request.method == "GET":
        booking_form = BookingForm()
        return render(request, 'booking.html', {"form": booking_form})

    elif request.method == "POST":
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking = booking_form.save()
            return render(request, "booking_detail.html", {"booking": booking})
        else:
            return render(request, 'booking.html', {"form": booking_form})


def homepage(request):
    return render(request, "home.html")
