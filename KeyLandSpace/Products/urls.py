from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('templates/ourprofile.html', view_our_profile),
	path('templates/contactus.html', view_contact_us),
	path('templates/catogories.html', view_catogories),
	path('templates/sell.html', view_sell),
	path('templates/buy.html', view_buy),
]