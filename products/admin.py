from django.contrib import admin
from .models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Product, ProductAdmin)
