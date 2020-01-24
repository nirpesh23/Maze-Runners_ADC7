from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
     path('productlist/edit/<int:ID>',view_productdata_updateform),
     path('productlist/edit/update/<int:ID>',view_update_form_data_in_db),
     path('productlist/',view_product_details),
     path('homepage/', view_homepage),
	
	 
]