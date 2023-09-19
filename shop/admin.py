from django.contrib import admin
from .models import Product, Category, Tag

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    #specifies which fields should be displayed in the admin list view for each model.
    list_display = ['name','price','date_added']
    # adds filters in the right sidebar to filter records by specific fields
    list_filter = ['date_added']
    #
    search_fields = ['name','description']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','description']
    search_fields = ['name',]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name',]
    search_fields = ['name',]




