"""CockapooClub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles import staticfiles_patterns


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('book_sessions.urls'), name='booking'),
    # path('booking_detail/', include('book_sessions.urls'), name='booking_detail'),

    path('', include('home.urls'), name='index'),
    # path('newCockaparents/', include('home.urls'), name='newCockaparents'),

    path('summernote/', include('django_summernote.urls')),
    path("accounts/", include("allauth.urls")),
]


urlpatterns += staticfiles_patterns


#   path(r'^admin/', admmin.site.urls),
#   path(r'^home/$', views.homepage),
#   path(r'^booking/$', views.booking)

#   path('admin/', admin.site.urls),
#   path("booking/", include("booking.urls")),
#   path('hello/', say_hello, name='hello'),

#     path(
#     'admin/password_reset/',
#    auth_views.PasswordResetView.as_view(),
#    name='admin_password_reset',
# ),

#    path(
#    'admin/password_reset/done/',
#    auth_views.PasswordResetDoneView.as_view(),
#    name='password_reset_done',
# ),

#     path(
#     'reset/<uidb64>/<token>/',
#     auth_views.PasswordResetConfirmView.as_view(),
#     name='password_reset_confirm',
# ),

#     path('reset/done/',
#     auth_views.PasswordResetCompleteView.as_view(),
#     name='password_reset_complete',
# ),
