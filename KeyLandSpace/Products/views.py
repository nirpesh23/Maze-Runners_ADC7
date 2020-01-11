from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context
from .models import Product

# Create your views here.
def view_our_profile(request):
	return render(request,'ourprofile.html')

def view_contact_us(request):
	return render(request,'contactus.html')