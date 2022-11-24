from django.shortcuts import render, HttpResponse, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponse
from django import Booking

# Create your views here.


def Booking(request):
    return HttpResponse('You are on the Booking a Session Page')


# class BookList(generic.ListView):
#     model = Book
#     queryset = Book.objects.filter(status=1).order_by("-created_on")
#     template_name = "booking.html"


# class Book(View):

#     def Book(self, request, slug, *args, **kwargs):
#         Book = get_object_or_404(Book, slug=slug)

#         return HttpResponseRedirect(reverse('post_detail', args=[slug]))
