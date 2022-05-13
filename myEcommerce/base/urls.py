from django.contrib import admin
from django.urls import path, include

from .views import Ecommerce

urlpatterns = [
    path('', Ecommerce.as_view(), name='ecommerce_url'),
]
