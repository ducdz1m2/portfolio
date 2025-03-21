from django.urls import path
from .views import *

urlpatterns = [
    path('', tools, name="tools"),
    path('word-counter/', word_counter, name='word_counter'),
]