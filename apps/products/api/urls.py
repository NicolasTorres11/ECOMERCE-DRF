from django.urls import path
from apps.products.api.views.generic_views import MeasureUnitListView, IndicatorListAPIView, CategoryProductListAPIView
from apps.products.api.views.products_views import (
    ListCreateProductAPIView,
    ProductRetrieveUpdateDestroyAPIView,
    # ProductDeleteAPIView,
    # ProductUpdateAPIView
)

urlpatterns = [
    path('measure_unit/', MeasureUnitListView.as_view(), name='Measure Unit'),
    path('indicator/', IndicatorListAPIView.as_view(), name='Indicator'),
    path('category_product/', CategoryProductListAPIView.as_view(), name='Product Category'),
    path('product/', ListCreateProductAPIView.as_view(), name='Create and List Product'),
    path('retrieve_update_destroy_product/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(),
         name='Retrieve Update and Destroy Product'),
    # path('delete_product/<int:pk>/', ProductDeleteAPIView.as_view(), name='Delete Product'),
    # path('update_product/<int:pk>/', ProductUpdateAPIView.as_view(), name='Update Product')
]
