from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('furryFunFotoGallery/', views.furryFunFotoGallery, name='Furry-Fun-Foto-Gallery'),
    path('newCockaparents/', views.newCockaparents, name='New-Cockaparents'),
    path('keepYourPooHealthy/', views.keepYourPooHealthy, name='Keep-your-Poo-Healthy'),
    # path('/templates/member-profile.html', views.DogProfile, name='dog-profile'),
]
