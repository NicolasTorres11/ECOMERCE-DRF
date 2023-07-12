from apps.base.api import GenericListAPIView
from apps.products.api.serializers.generic_serializers import IndicatorSerializer, CategoryProductSerializer, MeasureUnitSerializer


class MeasureListAPIView(GenericListAPIView):
    serializer_class = MeasureUnitSerializer


class IndicatorListAPIView(GenericListAPIView):
    serializer_class = IndicatorSerializer


class CategoryProductListAPIView(GenericListAPIView):
    serializer_class = CategoryProductSerializer

