from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product, Category, Comment
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


def is_valid_queryparam(param):
    return param != '' and param is not None


@login_required
def LikeView(request, pk):
    post = get_object_or_404(Product, id=request.POST.get('product_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('single_shop', args=[str(pk), str(post.slug)]))


class ShopView(LoginRequiredMixin, ListView):
    template_name = 'shop/category.html'
    model = Product
    paginate_by = 12
    extra_context = {'categories': Category.objects.all()}
    context_object_name = 'products'

    def get_queryset(self):
        view_count_min = self.request.GET.get('view_count_min')
        view_count_max = self.request.GET.get('view_count_max')

        queryset = Product.objects.all()

        if is_valid_queryparam(view_count_min):
            queryset = queryset.filter(price__gte=view_count_min)

        if is_valid_queryparam(view_count_max):
            queryset = queryset.filter(price__lt=view_count_max)

        return queryset


@login_required
def shop_category(request, slug):
    posts = Product.objects.filter(category__slug=slug)
    paginator = Paginator(posts, 12)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'shop/category.html', {'products': posts, 'categories': Category.objects.all(), 'page_obj': page_obj})


class ShopSearchResultsListView(LoginRequiredMixin, ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'shop/category.html'
    paginate_by = 3

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        return Product.objects.filter(
            Q(title__icontains=query)
        )


class ShopDetailView(LoginRequiredMixin, DetailView):
    template_name = 'shop/single-product.html'
    context_object_name = 'product'
    extra_context = {'comments': Comment}

    model = Product

    def get_context_data(self, *args, **kwargs):
        context = super(ShopDetailView, self).get_context_data()

        stuff = get_object_or_404(Product, id=self.kwargs['pk'])
        context['total_likes'] = stuff.total_likes()
        return context
