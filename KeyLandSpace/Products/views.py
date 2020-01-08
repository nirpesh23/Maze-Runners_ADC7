from django.shortcuts import render

# Create your views here.
def view_product_lists(request):
    list_of_products= products.objects.all()
    print(list_of_products)
    context_variable = {
        'products':list_of_products
    }
    return render(request,'products/products.html',context_variable)                