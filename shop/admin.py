from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    #specifies which fields should be displayed in the admin list view for each model.
    list_display = ['title','price','date_added']
    # adds filters in the right sidebar to filter records by specific fields
    list_filter = ['date_added']
    #
    search_fields = ['name','description']

admin.site.register(Category)
#admin.site.register(Tag)
admin.site.register(Review)





