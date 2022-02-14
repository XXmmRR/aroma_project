from django.urls import path, include
from .views import ShopView, ShopDetailView, shop_category

urlpatterns = [
    path('', ShopView.as_view(), name='shop'),
    path('category/<slug:slug>/', shop_category, name='shop_category'),
    path('<int:pk>/<slug:slug>/', ShopDetailView.as_view(), name='single_shop')
]
