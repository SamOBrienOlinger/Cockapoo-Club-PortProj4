from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking, name='all_bookings'),
    path('delete/<int:booking_id>', views.delete_booking, name="delete-booking"),
    path('update/<int:booking_id>', views.update_booking, name='update-booking'),

]
