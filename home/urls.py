from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.furry-fun-foto-gallery, name='furry-fun-foto-gallery'),
    path('', views.New-Cockaparents, name='New-Cockaparents'),
    path('', views.Keep-your-Poo-Healthy, name='Keep-your-Poo-Healthy'),
    # path('', views.join-form, name='join-form.'),
    # path('', views.login-members, name='login-members'),
]
