from . import views
from django.urls import path
from book_sessions import views

urlpatterns = [
    path('booking/', views.booking.as_view(), name="booking"),
]
