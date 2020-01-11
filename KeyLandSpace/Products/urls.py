from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    #path('product/',view_product_page),
    path('productlist/',view_product_details),
    path('productform/',view_product_form),
    path('productform/save',view_productlist_save),
    path('productsearch/',view_product_search),
    path('productsearch/search',view_search),
    path('view/<int:ID>',viewProductDetails),
    
]

