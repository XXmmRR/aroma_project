from django.contrib import admin
from django.urls import path, include
from .views import BlogListView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list')
]
