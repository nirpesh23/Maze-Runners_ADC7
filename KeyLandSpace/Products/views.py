from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context
from .models import Product



# Create your views here.
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

def view_product_page(request):
    return render(request,'products/product.html')

def view_product_details(request):
    product= Product.objects.all()
    print(product)
    context_variable = {
        'products':product
    }
    return render(request,'products/product.html',context_variable)



