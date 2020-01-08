from django.shortcuts import render

# Create your views here.
def view_product_lists(request):
    list_of_products= Products.objects.all()
    print(list_of_products)
    context_variable = {
        'flights':list_of_flights
    }
    return render(request,'flight/flights.html',context_variable)                