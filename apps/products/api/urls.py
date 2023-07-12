from django.urls import path
from apps.products.api.views.generic_views import MeasureListAPIView, IndicatorListAPIView, CategoryProductListAPIView
from apps.products.api.views.product_views import ProductListAPIView, CreateProductAPIView

urlpatterns = [
    path('measure_unit/', MeasureListAPIView.as_view(), name='Measure Unit'),
    path('indicator/', IndicatorListAPIView.as_view(), name='Indicators'),
    path('category_product/', CategoryProductListAPIView.as_view(), name='Category Products'),
    path('products_list/', ProductListAPIView.as_view(), name='List of Products'),
    path('create_product/', CreateProductAPIView.as_view(), name='Create Products'),
]
