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


# @login_required
# def  DogProfile(request):
#     if request.method == "GET":
#         dog_details =  DogProfile()
#         return render(request, '/templates/member-profile.html', {"form": dog_details})

#     elif request.method == "POST":
#         dog_details = DogProfile(request.POST)
#         if  dog_details.is_valid():
#             DogProfile = dog_details.save()
#             messages.add_message(request, messages.SUCCESS, 'your details have been saved')
#             return render(request, '/templates/member-profile.html', {"your details":  DogProfile})
#         else:
#             return render(request, '/templates/member-profile.html', {"form": dog_details})


# def join(request):
#     if request.method == "GET":
#        A_A = B()
#        return render(request, '/templates/member-profile.html', {"form": A_A}))
    #   elif request.method == "POST":
    #     A_A = B(request.POST)
    #     if A_A.is_valid():
    #         DogProfile = A_A.save()

    # elif request.method == "POST":
    #     A_A = B(request.POST)
    #     if B.is_valid():
    #         DogProfile = B.save()
    #         messages.add_message(request, messages.SUCCESS, 'You are now a member of Cockapoo Club')
    #         return render(request, 'account_X.html', {"booking": DogProfile})
    #     else:
    #         return render(request, '', {"form": A_A})


# def Login(request):
#     if request.method == 'POST':

    # return render(request, '/templates/member-profile.html', context)

# @login_required
# def Logout(request):
#     logout(request)
#     return redirect('account_login')
