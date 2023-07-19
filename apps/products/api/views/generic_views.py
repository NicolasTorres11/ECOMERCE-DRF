from apps.base.api import GenericListAPIView
from apps.products.api.serializers.generic_serializers import IndicatorSerializer, CategoryProductSerializer, MeasureUnitSerializer
from rest_framework import viewsets


class MeasureListAPIView(viewsets.ModelViewSet):
    serializer_class = MeasureUnitSerializer


class IndicatorListAPIView(viewsets.ModelViewSet):
    serializer_class = IndicatorSerializer


class CategoryProductListAPIView(viewsets.ModelViewSet):
    serializer_class = CategoryProductSerializer



