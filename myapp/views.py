from django.shortcuts import render
from .models import *

# Create your views here.
def Home(request):
    tables = Table.objects.all()
    menu_items = MenuItem.objects.all()
    context = {
        'table': tables,
        'menu_item': menu_items
    }
    return render(request, 'home.html', context)

def Order(request, table_id, menu_item_id):
    table = Table.objects.get(id=table_id)
    menu_item = MenuItem.objects.get(id=menu_item_id)
    Order.objects.create(table=table, menu_item=menu_item, quantity=1)
    context = {
        'table' : table,
        'menu_item' : menu_item
    }
    
    return render(request, 'order.html', context)

def Base(request):
    return render(request, "base.html")
