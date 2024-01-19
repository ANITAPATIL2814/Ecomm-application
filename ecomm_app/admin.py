from django.contrib import admin 
from .models import product

# Register your models here.
#admin.site.register(product)

# list display
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','price','cat','is_active']
    #filter 
    list_filter=['cat','is_active']
admin.site.register(product,ProductAdmin)
