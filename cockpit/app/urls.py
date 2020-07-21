from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Home, name='home-page'),
    path('login/', Login, name='login'),
]
