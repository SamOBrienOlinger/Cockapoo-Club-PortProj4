from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect

# Create your views here.


class BookList(generic.ListView):
    model = Book
    queryset = Book.objects.filter(status=1).order_by("-created_on")
    template_name = "booking.html"


def index(request):
    return HttpResponse("Hello world!")
