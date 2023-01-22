from django.urls import path
from . import views

urlpatterns = [
    path('booking/', views.booking, name='booking'),
    path('booking/delete/<int:id>', views.delete_booking, name="delte-booking"),
    path('booking/<int:id>', views.update_booking, name='update-booking'),
    path('', views.homepage, name='homepage'),
    # path('booking_detail/', views.booking, name='booking_detail'),
]
