from django.urls import path
from . import views

urlpatterns = [
    path('booking/', views.booking, name='booking'),
    path('', views.homepage, name='homepage'),
    # path('booking_detail/', views.booking, name='booking_detail'),
]
