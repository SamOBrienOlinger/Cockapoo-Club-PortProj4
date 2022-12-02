from django.shortcuts import render, HttpResponse, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponse
from .models import homepage

# Create your views here.


def homepage(request):
    return render(request, "index.html")
