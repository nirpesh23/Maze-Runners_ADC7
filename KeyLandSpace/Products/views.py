from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context
from .models import Products

# Create your views here.
def view_product_lists(request):
    list_of_products= Products.objects.all()
    print(list_of_products)
    context_variable = {
        'products':list_of_products
    }
    return render(request,'products/products.html',context_variable)   
                 