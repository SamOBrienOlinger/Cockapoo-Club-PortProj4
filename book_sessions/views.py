# from django.shortcuts import render, get_object_or_404, reverse
# from django.views import generic, View
# from django.http import HttpResponseRedirect
# from django.http import Book

from django.http import HttpResponse

# Create your views here.


def booking(request):
    return HttpResponse('Booking')


# class BookList(generic.ListView):
#     model = Book
#     queryset = Book.objects.filter(status=1).order_by("-created_on")
#     template_name = "booking.html"


# class Book(View):

#     def Book(self, request, slug, *args, **kwargs):
#         Book = get_object_or_404(Book, slug=slug)

#         return HttpResponseRedirect(reverse('post_detail', args=[slug]))
