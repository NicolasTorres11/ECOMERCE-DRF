from django.urls import path
from apps.products.api.views.generic_views import MeasureListAPIView, IndicatorListAPIView, CategoryProductListAPIView
from apps.products.api.views.product_views import (
    CreateListProductAPIView,
    ProductDetailAPIView,
)

urlpatterns = [
    path('measure_unit/', MeasureListAPIView.as_view(), name='Measure Unit'),
    path('indicator/', IndicatorListAPIView.as_view(), name='Indicators'),
    path('category_product/', CategoryProductListAPIView.as_view(), name='Category Products'),
    path('products/', CreateListProductAPIView.as_view(), name='Create and List Products'),
    path('detail_update_delete_product/<int:pk>/', ProductDetailAPIView.as_view(), name='Detail of products'),
]
