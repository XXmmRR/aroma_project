from django.urls import path, include
from .views import ShopView

urlpatterns = [
    path('', ShopView.as_view(), name='shop')
]
