from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username","email","password1","password2"),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Review)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart)
admin.site.register(Cartitems)
admin.site.register(get_user_model(),CustomUserAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)





