from apps.products.api.serializers.generic_serializers import MeasureUnitSerializer, IndicatorSerializer, CategoryProductSerializer
from apps.base.api import GeneralListAPIView

class MeasureUnitListView(GeneralListAPIView):
    serializer_class = MeasureUnitSerializer


class IndicatorListAPIView(GeneralListAPIView):
    serializer_class = IndicatorSerializer


class CategoryProductListAPIView(GeneralListAPIView):
    serializer_class = CategoryProductSerializer

