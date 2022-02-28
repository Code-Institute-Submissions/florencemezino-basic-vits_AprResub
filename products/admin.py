from django.contrib import admin
from .models import Product, Category, HealthGoal, Package


class ProductAdmin(admin.ModelAdmin):
    """ product admin docstring """
    product_tags = ['immunity', 'brain', 'energy', 'eyes', 'sleep', 'stress', 'heart', 'joints', 'skin', 'hair', 'digestion', 'bones', 'shape', 'summer', 'spring', 'autumn', 'winter', ]
    list_display = (
        'sku',
        'name',
        'description_benefits',
        'category',
        'quantity',
        'price',
        'image',
    )

    ordering = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class HealthGoalAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class PackageAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(HealthGoal, HealthGoalAdmin)
admin.site.register(Package, PackageAdmin)