from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context
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