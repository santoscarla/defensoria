from django.urls import path
from . import views

urlpatterns = [
    path('', principal, name='principal'),
]