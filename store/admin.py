from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','category_id']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','phone']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['product_id','user_id', 'phone','quantity','price','order_date']

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
