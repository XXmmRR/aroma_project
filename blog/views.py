from django.db.models import Q
from .models import BlogModel, Comment
from django.views.generic import ListView, DetailView
from taggit.models import Tag
from django.db.models import Count


class TagMixin(object):
    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


class BlogListView(TagMixin, ListView):
    model = BlogModel
    template_name = 'blog.html'
    paginate_by = 3
    queryset = BlogModel.objects.annotate(num_comments=Count('comments')).all()
    context_object_name = 'posts'


class BlogDetailView(TagMixin, DetailView):
    model = BlogModel
    queryset = BlogModel.objects.annotate(num_comments=Count('comments')).all()
    template_name = 'blog-detail.html'
    context_object_name = 'post'


class SearchResultsListView(TagMixin, ListView):
    model = BlogModel
    context_object_name = 'posts'
    template_name = 'blog.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        return BlogModel.objects.filter(
            Q(title__icontains=query)
        )


class TagIndexView(TagMixin, ListView):
    model = BlogModel
    template_name = 'blog.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        queryset = BlogModel.objects.annotate(num_comments=Count('comments')).all()
        return queryset.filter(tags__slug=self.kwargs.get('tag_slug'))
