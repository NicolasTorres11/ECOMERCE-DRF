from rest_framework import serializers
from apps.products.models import Product
from apps.products.api.serializers.generic_serializers import MeasureUnitSerializer, CategoryProductSerializer, IndicatorSerializer


class ProductSerializer(serializers.ModelSerializer):
    # # METODO 2 PARA SERIALIZAR UNA LLAVE FOREANEA
    # measure_unit = serializers.StringRelatedField()
    #
    # # METODO 1 PARA SERIALIZAR UNA LLAVE FOREANEA
    # category_product = CategoryProductSerializer()

    class Meta:
        model = Product
        exclude = ('state', 'created_date', 'updated_date', 'deleted_date')

    # METODO 3 PARA SERIALIZAR UN MODELO CON UNA LLAVE FORANEA
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            'product_image': instance.product_image if instance.product_image != '' else '',
            'measure_unit': instance.measure_unit.description,
            'category_product': instance.category_product.description
        }