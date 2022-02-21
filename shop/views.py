from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Category, Comment
from django.db.models import Q
from django.core.paginator import Paginator


# Create your views here.


class ShopView(ListView):
    template_name = 'shop/category.html'
    model = Product
    paginate_by = 12
    extra_context = {'categories': Category.objects.all()}
    context_object_name = 'products'


def shop_category(request, slug):
    posts = Product.objects.filter(category__slug=slug)
    paginator = Paginator(posts, 12)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'shop/category.html', {'products': posts, 'categories': Category.objects.all(), 'page_obj': page_obj})


class ShopSearchResultsListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'shop/category.html'
    paginate_by = 12

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        return Product.objects.filter(
            Q(title__icontains=query)
        )


class ShopDetailView(DetailView):
    model = Product
    template_name = 'shop/single-product.html'
    context_object_name = 'product'
    extra_context = {'comments': Comment}
