from django.urls import path, include
from .views import ShopView, ShopDetailView, shop_category, ShopSearchResultsListView, LikeView

urlpatterns = [
    path('', ShopView.as_view(), name='shop'),
    path('category/<slug:slug>/', shop_category, name='shop_category'),
    path('search/', ShopSearchResultsListView.as_view(), name='shop_search_results'),
    path('<int:pk>/<slug:slug>/', ShopDetailView.as_view(), name='single_shop'),
    path('like/<int:pk>/', LikeView, name='product_like')
]
