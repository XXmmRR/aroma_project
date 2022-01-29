from django.views.generic import CreateView
from .models import BlogModel


class CreateBlogView(CreateView):
    model = BlogModel
