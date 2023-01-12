from django.shortcuts import render, HttpResponse, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponse
from .models import index
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# from .forms import DogProfile

# Create your views here.


def index(request):
    return render(request, "index.html")


def newCockaparents(request):
    return render(request, "new-cockaparents.html")


def keepYourPooHealthy(request):
    return render(request, "keep-your-poo-healthy.html")


@login_required
def furryFunFotoGallery(request):
    return render(request, "furry-fun-foto-gallery.html")


# def join(request):
#     if request.method == 'POST':


# def Login(request):
#     if request.method == 'POST':

# def Logout(request):
#     logout(request)
#     return redirect('account_login')
