from django.urls import path
from . import views

urlpatterns = [
    path('booking/', views.booking, name='booking'),
    path('', views.homepage, name='homepage'),
    # path('', views.booking_detail, name='booking_detail'),
]

# # from django.urls import path, include
# from book_sessions import views

# urlpatterns = [
#     path('booking/', views.booking.as_view(), name="booking"),
#     path('booking/', include('booking.urls')),
# ]
