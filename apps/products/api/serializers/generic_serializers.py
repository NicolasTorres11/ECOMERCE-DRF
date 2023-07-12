from rest_framework import serializers
from apps.products.models import MeasureUnit, CategoryProduct, Indicator


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
            'descount_value': instance.descount_value,
            'category_product': instance.category_product.description
        }


class CategoryProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryProduct
        exclude = ('state', 'created_date', 'updated_date', 'deleted_date')

    def to_representation(self, instance):
        return {
            'description': instance.description,
            'measure_unit': instance.measure_unit.description
        }
