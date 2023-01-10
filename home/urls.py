from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('furryFunFotoGallery/', views.furryFunFotoGallery, name='Furry-Fun-Foto-Gallery'),
    path('newCockaparents/', views.newCockaparents, name='New-Cockaparents'),
    path('keepYourPooHealthy/', views.keepYourPooHealthy, name='Keep-your-Poo-Healthy'),
    # path('account_signup/', views.DogProfile, name='dog_profile'),

    # path('member-profile/', views.memberProfile, name='member-profile'),
    # path('account/login/', views.login, name='account_login'),
    # path('', views.join-form, name='join-form.'),
    # path('', views.login-members, name='login-members'),
]
