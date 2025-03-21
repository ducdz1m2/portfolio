from django.urls import path
from .views import *
urlpatterns = [
    path('', ai, name='ai')
]