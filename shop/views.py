from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Category

# Create your views here.


class ShopView(ListView):
    template_name = 'shop/category.html'
    model = Product
    paginate_by = 12
    extra_context = {'categories': Category.objects.all()}
    context_object_name = 'products'


def shop_category(request, slug):
    posts = Product.objects.filter(category__slug=slug)
    menu = Category.objects.all()
    return render(request, 'shop/category.html', {'products': posts, 'categories': menu})


class ShopDetailView(DetailView):
    model = Product
    template_name = 'shop/single-product.html'
    context_object_name = 'product'
