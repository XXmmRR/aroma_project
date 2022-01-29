from .views import HomePageView, AboutPageView
from django.urls import path

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contact/', AboutPageView.as_view(), name='contact')
]
