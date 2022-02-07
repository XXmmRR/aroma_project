from django.contrib import admin
from django.urls import path, include
from .views import BlogListView, TagIndexView, BlogDetailView, SearchResultsListView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('tags/<slug:tag_slug>/', TagIndexView.as_view(), name='post_by_tag'),
    path('post/<int:pk>/<slug:slug>/',
         BlogDetailView.as_view(), name='post_detail'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
    ]
