# # from django.urls import path, include
# from book_sessions import views

# urlpatterns = [
#     path('booking/', views.booking.as_view(), name="booking"),
#     path('booking/', include('booking.urls')),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking, name='booking'),
    path('', views.homepage, name='homepage'),
]
