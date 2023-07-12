from rest_framework import serializers
from apps.products.models import Product
from apps.products.api.serializers.generic_serializers import MeasureUnitSerializer, CategoryProductSerializer


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = ('state', 'created_date', 'updated_date', 'deleted_date')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            'product_image': instance.product_image if instance.product_image != '' else '',
            'measure_unit': instance.measure_unit.description,
            'category_product': instance.category_product.description
        }
