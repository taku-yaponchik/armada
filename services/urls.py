from django.urls import path
from .views import *

urlpatterns = [
    path('service/', services_list, name='services_list')
]