from django.shortcuts import render
from django.views.generic import ListView
from .models import Product, Category
from django.db.models import Count

# Create your views here.


class ShopView(ListView):
    template_name = 'shop/category.html'
    model = Product
    queryset = Product.objects.annotate(num_products=Count('product_type')).all()
    extra_context = {'categories': Category.objects.all()}
    context_object_name = 'products'
