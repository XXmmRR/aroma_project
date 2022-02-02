from django.db.models import Q
from .models import BlogModel
from django.views.generic import ListView, DetailView
from taggit.models import Tag


class BlogListView(ListView):
    model = BlogModel
    template_name = 'blog.html'
    paginate_by = 3
    queryset = BlogModel.objects.all()
    context_object_name = 'posts'


class BlogDetailView(DetailView):
    model = BlogModel
    template_name = 'blog-detail.html'
    context_object_name = 'post'


class SearchResultsListView(ListView):
    model = BlogModel
    context_object_name = 'posts'
    template_name = 'blog.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        return BlogModel.objects.filter(
            Q(title__icontains=query)
        )


class TagIndexView(ListView):
    model = BlogModel
    template_name = 'blog.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return BlogModel.objects.filter(tags__slug=self.kwargs.get('tag_slug'))
