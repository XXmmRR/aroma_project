from django.urls import path, include
from .views import ShopView, ShopDetailView, shop_category, ShopSearchResultsListView, LikeView, cart_add, item_clear,\
item_increment, cart_clear, cart_detail, item_decrement, payment


urlpatterns = [
    path('', ShopView.as_view(), name='shop'),
    path('category/<slug:slug>/', shop_category, name='shop_category'),
    path('search/', ShopSearchResultsListView.as_view(), name='shop_search_results'),
    path('<int:pk>/<slug:slug>/', ShopDetailView.as_view(), name='single_shop'),
    path('like/<int:pk>/', LikeView, name='product_like'),
    path('cart/add/<int:id>/', cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         item_decrement, name='item_decrement'),
    path('cart/cart_clear/', cart_clear, name='cart_clear'),
    path('cart/cart-detail/', cart_detail, name='cart_detail'),
    path('cart/payment', payment, name='payment')
]
