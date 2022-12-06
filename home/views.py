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


def join(request):
    return render(request, "signup.html")


def login(request):
    return render(request, "login.html")

# def join(request):
#     return render(request, "join-form.html")


# def login(request):
#     return render(request, "login-members.html")
