from django.shortcuts import render
from django.http import HttpResponse

from .models import Categories, Customers, Inventory, \
                    Products, Reorder, CustomerHistory, \
                    Orders, OrderLines

# Create your views here.

def check_db(request):
    category_list = Categories.objects.all()
    print("Categories")
    for category_item in category_list:
        print(category_item)
    print()
    print("-"*80)
    print()

    print("Customers")
    customer_list = Customers.objects.all()[:10]
    for customer_item in customer_list:
        print(customer_item)
    print()
    print("-"*80)
    print()

    print("Inventory")
    inventory_list = Inventory.objects.all()[:10]
    for inventory_item in inventory_list:
        print(inventory_item)
    print()
    print("-"*80)
    print()

    print("Products")
    product_list = Products.objects.all()[:10]
    for product_item in product_list:
        print(product_item)

    print()
    print("-"*80)
    print()
    print("Reorder")
    reorder_list = Reorder.objects.all()[:10]
    for reorder_item in reorder_list:
        print(reorder_item)

    print()
    print("-"*80)
    print()
    print("Customer history")
    custhist_list = CustomerHistory.objects.all()[:10]
    for custhist_item in custhist_list:
        print(custhist_item)

    print()
    print("-"*80)
    print()
    print("Orders")
    order_list = Orders.objects.all()[:10]
    for order_item in order_list:
        print(order_item)

    print()
    print("-"*80)
    print()
    print("OrderLines")
    orderlines_list = OrderLines.objects.all()[:10]
    for orderlines_item in orderlines_list:
        print(orderlines_item)

    return HttpResponse("Checked")
