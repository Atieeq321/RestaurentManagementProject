from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ["number", "capacity", "is_reserved"]

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "price"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["table", "menu_item", "quantity", "created_at"]

