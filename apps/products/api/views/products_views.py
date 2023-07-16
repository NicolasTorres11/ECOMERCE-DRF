from apps.products.api.serializers.product_serializers import ProductSerializer
from apps.base.api import GeneralListAPIView


class ProductListAPIView(GeneralListAPIView):
    serializer_class = ProductSerializer
    
    