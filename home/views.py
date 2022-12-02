from django.shortcuts import render, HttpResponse, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponse
from .models import index

# Create your views here.


def index(request):
    return render(request, "index.html")
