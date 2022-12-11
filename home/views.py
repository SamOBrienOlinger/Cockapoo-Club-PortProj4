from django.shortcuts import render, HttpResponse, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponse
from .models import index

# Create your views here.


def index(request):
    return render(request, "index.html")


def newCockaparents(request):
    return render(request, "new-cockaparents.html")


def keepYourPooHealthy(request):
    return render(request, "keep-your-poo-healthy.html")


def furryFunFotoGallery(request):
    return render(request, "furry-fun-foto-gallery.html")


def memberProfile(request):
    return render(request, "member-profile.html")


# def booking(request):
#     if request.method == "GET":
#         booking_form = BookingForm()
#         return render(request, 'booking.html', {"form": booking_form})

#     elif request.method == "POST":
#         booking_form = BookingForm(request.POST)
#         if booking_form.is_valid():
#             booking = booking_form.save()
#             return render(request, "booking_detail.html", {"booking": booking})
#         else:
#             return render(request, 'booking.html', {"form": booking_form})


# def homepage(request):
#     return render(request, "index.html")
