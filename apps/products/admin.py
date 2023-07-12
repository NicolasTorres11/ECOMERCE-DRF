from django.contrib import admin
from apps.products.models import Product, CategoryProduct, Indicator, MeasureUnit


class MeasureUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')


class CategoryProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'measure_unit')


class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'product_image', 'measure_unit', 'category_product')


class IndicatorModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'descount_value', 'category_product')


admin.site.register(Product, ProductModelAdmin)
admin.site.register(CategoryProduct, CategoryProductAdmin)
admin.site.register(Indicator, IndicatorModelAdmin)
admin.site.register(MeasureUnit, MeasureUnitAdmin)
