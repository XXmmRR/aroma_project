from django.db.models import Q
from .models import BlogModel, Comment, IpModel
from django.views.generic import ListView, DetailView, CreateView
from taggit.models import Tag
from django.db.models import Count
from .forms import CommentForm

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


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
    extra_context = {'form': CommentForm}
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        ip = get_client_ip(self.request)
        print(ip)
        if IpModel.objects.filter(ip=ip):
            print('Ip already present')
            post_id = request.GET.get('post_id')
            post = BlogModel.objects.get(id=post_id)
            post.views.add(IpModel.objects.get(ip=ip))
        else:
            IpModel.objects.create(ip=ip)
            post_id = request.GET.get('post_id')
            post = BlogModel.objects(id=post_id)
            post.views.add(IpModel.get(ip=ip))
        return self.render_to_response(context)


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

