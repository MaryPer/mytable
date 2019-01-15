#Схема URL для table
from django.urls import path
from . import views

urlpatterns = [
#home page
    path('', views.index, name='index'),
]