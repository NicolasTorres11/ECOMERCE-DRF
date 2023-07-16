from django.contrib import admin
from apps.products.models import Product, CategoryProduct, Indicator, MeasureUnit


class MeasureAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')


class IndicatorAdmin(admin.ModelAdmin):
    list_display = ('id', 'discount_value', 'category_product')


class CategoryProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'measure_unit')


admin.site.register(Product)
admin.site.register(CategoryProduct, CategoryProductsAdmin)
admin.site.register(Indicator, IndicatorAdmin)
admin.site.register(MeasureUnit, MeasureAdmin)

