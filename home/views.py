from django.shortcuts import render, HttpResponse, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponse
from .models import index

# Create your views here.


def index(request):
    return render(request, "index.html")


# def index(request):
#     return render(request, "New Cockaparents.html")


# def index(request):
#     return render(request, ".Keep your Poo Healthyhtml")


# def index(request):
#     return render(request, "Furry Fun Foto Gallery.html")


# def index(request):
#     return render(request, "Join.html")


# def index(request):
#     return render(request, "Login.html")
