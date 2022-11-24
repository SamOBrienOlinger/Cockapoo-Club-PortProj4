from django.shortcuts import render, HttpResponse, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponse
# from django import home

# Create your views here.


def homepage(request):
    return HttpResponse('You are on the Homepage')
