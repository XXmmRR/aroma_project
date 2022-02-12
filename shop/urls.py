from django.urls import path, include
from .views import ShopView, ShopDetailView

urlpatterns = [
    path('', ShopView.as_view(), name='shop'),
    path('/<int:pk>/', ShopDetailView.as_view(), name='single_shop')
]
