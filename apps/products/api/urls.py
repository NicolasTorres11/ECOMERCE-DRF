from django.urls import path
from apps.products.api.views.generic_views import MeasureListAPIView, IndicatorListAPIView, CategoryProductListAPIView
from apps.products.api.views.product_views import (
    ProductListAPIView,
    CreateProductAPIView,
    ProductDetailAPIView,
    DestroyProductAPIView,
    ProductUpdateAPIView
)

urlpatterns = [
    path('measure_unit/', MeasureListAPIView.as_view(), name='Measure Unit'),
    path('indicator/', IndicatorListAPIView.as_view(), name='Indicators'),
    path('category_product/', CategoryProductListAPIView.as_view(), name='Category Products'),
    path('products_list/', ProductListAPIView.as_view(), name='List of Products'),
    path('create_product/', CreateProductAPIView.as_view(), name='Create Products'),
    path('detail_product/<int:pk>/', ProductDetailAPIView.as_view(), name='Detail of products'),
    path('delete_product/<int:pk>/', DestroyProductAPIView.as_view(), name='Delete Product'),
    path('update_product/<int:pk>/', ProductUpdateAPIView.as_view(), name='Update Products')
]
