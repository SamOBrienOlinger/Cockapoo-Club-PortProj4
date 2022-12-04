from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.furryFunFotoGallery, name='Furry-Fun-Foto-Gallery'),
    path('', views.newCockaparents, name='New-Cockaparents'),
    path('', views.keepYourPooHealthy, name='Keep-your-Poo-Healthy'),
    # path('', views.join-form, name='join-form.'),
    # path('', views.login-members, name='login-members'),
]
