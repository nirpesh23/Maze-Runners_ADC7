from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context
from .models import Product

# Create your views here.
def view_homepage(request):
	return render(request,'homepage.html')

def view_hello_world(request):
    return HttpResponse("Hello World")
    
def view_productdata_updateform(request,ID):
    print(ID)
    product_obj = Product.objects.get(id=ID)
    print(product_obj)
    context_varible = {
        'product':product_obj
    }
    return render(request,'products/productupdateform.html',context_varible)

def view_update_form_data_in_db(request,ID):
    product_obj = Product.objects.get(id=ID)
    print(product_obj)
    product_form_data = request.POST
    print(product_form_data)
    product_obj.origin = request.POST['Name']
    product_obj.destination =request.POST['Condition']
    product_obj.duration = request.POST['Price']
    product_obj.save()

    return HttpResponse("Record Updated!!")

