from django.contrib import admin

from .models import Category, Product

# admin.site.register(Product)


class ProductInline(admin.StackedInline):
    model = Product
    extra = 3


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Category', {'fields': ['name']}),
    ]
    inlines = [ProductInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)
