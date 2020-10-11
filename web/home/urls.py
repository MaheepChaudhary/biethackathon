from .views import *
from django.urls import path

urlpatterns = [
    path('',home,name='home'),
    path('predict',predict,name='predict'),
    path('search', search, name = 'search')
]
