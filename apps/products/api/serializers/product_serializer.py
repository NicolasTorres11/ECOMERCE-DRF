from rest_framework import serializers
from apps.products.models import Product
from apps.products.api.serializers.generic_serializers import MeasureUnitSerializer, CategoryProductSerializer


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = ('state', 'created_date', 'updated_date', 'deleted_date')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['measure_unit'] = instance.measure_unit.description if instance.measure_unit is not None else ''
        data['category_product'] = instance.category_product.description if instance.category_product is not None else ''
        if not instance.product_image:
            data['product_image'] = ''
        return data
