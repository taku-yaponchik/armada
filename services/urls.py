from django.urls import path
from .views import *

urlpatterns = [
    path('', services_list, name='services_list'),
    path('portfolio', portfolio_list, name='portfolio_panel')
]