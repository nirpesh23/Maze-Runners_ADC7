from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('productlist/', view_product_lists),
]