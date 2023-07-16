from django.urls import path
from apps.products.api.views.generic_views import MeasureUnitListView, IndicatorListAPIView, CategoryProductListAPIView
from apps.products.api.views.products_views import ProductListAPIView

urlpatterns = [
    path('measure_unit/', MeasureUnitListView.as_view(), name='Measure Unit'),
    path('indicator/', IndicatorListAPIView.as_view(), name='Indicator'),
    path('category_product/', CategoryProductListAPIView.as_view(), name='Product Category'),
    path('products_list/', ProductListAPIView.as_view(), name='List of Products')
]
