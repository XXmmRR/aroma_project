from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Category

# Create your views here.


class ShopView(ListView):
    template_name = 'shop/category.html'
    model = Product
    extra_context = {'categories': Category.objects.all()}
    context_object_name = 'products'


class ShopDetailView(DetailView):
    model = Product
    template_name = 'shop/single-product.html'
    context_object_name = 'product'
