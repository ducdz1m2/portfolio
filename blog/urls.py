from django.urls import path
from .views import *
urlpatterns = [
   path('', BlogListView.as_view(), name='blog'),
   path('blog/<int:pk>/', post_detail, name='post_detail'),
]