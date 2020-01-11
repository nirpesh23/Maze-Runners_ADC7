from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context
from .models import Product

# Create your views here.
def view_our_profile(request):
	return render(request,'ourprofile.html')

def view_contact_us(request):
	return render(request,'contactus.html')

def view_catogories(request):
	return render(request,'catogories.html')

def view_sell(request):
	return render(request,'sell.html')

def view_buy(request):
	return render(request,'buy.html')
