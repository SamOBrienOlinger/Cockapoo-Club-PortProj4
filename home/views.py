from django.shortcuts import render, HttpResponse, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect

# Create your views here.


def say_hello(request):
    return HttpResponse("Hello!")
