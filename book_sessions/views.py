from django.shortcuts import render, HttpResponse, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponse
from django import booking

# Create your views here.


def booking(request):
    return render(request, 'booking.html', {})
