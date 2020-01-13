from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import Product



# Create your views here.

def view_product_page(request):
    return render(request,'products/prouct.html')

def view_product_details(request):
    list_of_product= Product.objects.all()
    print(list_of_product)
    context_variable = {
        'products':list_of_product
    }
    return render(request,'products/product.html',context_variable)

def view_product_form(request):
    return render(request,'products/productform.html')

def view_productlist_save(request):
    if request.method == "POST":
        get_all = request.POST
        get_Name = request.POST['products_Name']
        print(type(get_Name))
        get_Condition = request.POST['products_Condition']
        print(type(get_Condition))
        get_Price = request.POST['products_Price']
        print(type(get_Price))
        products_obj = Product(Name=get_Name,Condition=get_Condition,Price=get_Price)
        products_obj.save()
        return HttpResponse("Record Save")

    else:
        return HttpResponse("Error record saving")    

def view_product_search(request):
    return render(request,'products/productform.html')

def viewProductDetails(request,ID):
    products = Product.objects.get(id=ID)
    context_varible = {'product':products}
    return render(request,'viewproduct/productsearch.html',context_varible)


def view_search(request):

    list_of_product = request.GET['search']
    products = Product.filter(text__icontains=list_of_product)

    context = {
    'products': products,
    'list_of_product': list_of_product
     }

    return render(request, 'products/productsearch.html', context)
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

