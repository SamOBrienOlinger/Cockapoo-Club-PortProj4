# from django.shortcuts import render, HttpResponse, get_object_or_404, reverse
# from django.views import generic, View
from django.http import HttpResponseRedirect

# Create your views here.


def homepage(request):
    return HttpResponse('homepage')
