# from . import views
# from django.urls import path
# from home import views

# urlpatterns = [
#     path('', views.homepage, name="homepage"),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
]
