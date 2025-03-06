from django.contrib import admin
from .models import User, Product

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password')
    search_fields = ['username', 'email']

class ProductAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'category', 'price')
    search_fields = ['name', 'category', 'description']

admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
