# from . import views
# # from django.urls import path, include
from book_sessions import views

# urlpatterns = [
#     path('booking/', views.booking.as_view(), name="booking"),
#     path('booking/', include('booking.urls')),
# ]

from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('booking/', views.booking, name='booking'),
]
