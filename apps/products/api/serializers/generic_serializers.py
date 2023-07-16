from rest_framework import serializers
from apps.products.models import MeasureUnit, Indicator, CategoryProduct


class MeasureUnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = MeasureUnit
        exclude = ('state', 'created_date', 'updated_date', 'deleted_date')


class IndicatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Indicator
        exclude = ('state', 'created_date', 'updated_date', 'deleted_date')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'discount_value': instance.discount_value,
            'category_product': instance.category_product.description
        }


class CategoryProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryProduct
        exclude = ('state', 'created_date', 'updated_date', 'deleted_date')

    # METODO 3 PARA SERIALIZAR UNA LLAVE FORANEA
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'description': instance.description,
            'measure_unit': instance.measure_unit.description
        }