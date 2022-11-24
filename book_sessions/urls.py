from . import views
from django.urls import path
from booking import views

urlpatterns = [
    path('booking/', views.Booking.as_view(), name="Booking"),
]
