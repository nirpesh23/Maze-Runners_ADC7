from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
     path('productdata/edit/<int:ID>',view_productdata_updateform),
     path('productdata/edit/update/<int:ID>',view_update_form_data_in_db),

     path('templates/homepage.html', view_homepage),
	
	 
]