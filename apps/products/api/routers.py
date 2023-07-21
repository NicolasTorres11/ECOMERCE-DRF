from rest_framework.routers import DefaultRouter
from apps.products.api.views.product_views import ProductViewSet
from apps.products.api.views.generic_views import *

router = DefaultRouter()

router.register(r'products', ProductViewSet, basename='products')
router.register(r'measure_unit', MeasureListViewSet, basename='measure_unit')
router.register(r'category_products', CategoryProductViewSet, basename='category_products')
router.register(r'indicators', IndicatorViewSet, basename='indicators')


urlpatterns = router.urls
