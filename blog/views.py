from django.shortcuts import render
from .models import BlogModel
from django.views.generic import ListView


class BlogListView(ListView):
    template_name = 'blog.html'
    model = BlogModel

