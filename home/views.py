from django.shortcuts import render, HttpResponse, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponse
from .models import index

# Create your views here.


def index(request):
    return render(request, "index.html")


def newCockaparents(request):
    return render(request, "New-Cockaparents.html")


def keepYourPooHealthy(request):
    return render(request, "Keep-your-Poo-Healthy.html")


def furryFunFotoGallery(request):
    return render(request, "Furry-Fun-Foto-Gallery.html")


# def join(request):
#     return render(request, "join-form.html")


# def login(request):
#     return render(request, "login-members.html")
