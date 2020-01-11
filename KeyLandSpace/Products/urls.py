from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('templates/ourprofile.html', view_our_profile),
	path('templates/contactus.html', view_contact_us),
	
]