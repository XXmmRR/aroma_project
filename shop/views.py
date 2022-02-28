from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Product, Category, Comment, Review
from django.db.models import Q
from django.core.paginator import Paginator
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RateForm
from cart.cart import Cart
from django.http import HttpResponseRedirect, HttpResponse
from cart.context_processor import cart_total_amount

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
    paginate_by = 12

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        return Product.objects.filter(
            Q(name__icontains=query)
        )


class ShopDetailView(LoginRequiredMixin, DetailView):
    template_name = 'shop/single-product.html'
    context_object_name = 'product'
    extra_context = {'comments': Comment, 'reviews': Review, 'form': RateForm}
    model = Product

    def post(self, request, *args, **kwargs):
        form = RateForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()

            return HttpResponseRedirect(reverse('single_shop', args=[str(post.id), str(post.slug)]))
        else:
            post = self.get_object()
            return HttpResponseRedirect(reverse('single_shop', args=[str(post.id), str(post.slug)]))

    def get_context_data(self, *args, **kwargs):
        context = super(ShopDetailView, self).get_context_data()

        stuff = get_object_or_404(Product, id=self.kwargs['pk'])
        context['total_likes'] = stuff.total_likes()

        return context


@login_required
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')

@login_required
def payment(request):
    return HttpResponse("Вы провели оплату")
