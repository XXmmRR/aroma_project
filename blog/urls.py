from django.contrib import admin
from django.urls import path, include
from .views import BlogListView, TagIndexView, BlogDetailView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('tags/<slug:tag_slug>/', TagIndexView.as_view(), name='post_by_tag'),
    path('post/<int:year>/<int:month>/<int:day>/<slug:slug>/',
         BlogDetailView.as_view(), name='post_detail')]
