from django.urls import path
from apps.products.api.views.generic_views import MeasureListAPIView, IndicatorListAPIView, CategoryProductListAPIView

urlpatterns = [
    path('measure_unit/', MeasureListAPIView.as_view(), name='Measure Unit'),
    path('indicator/', IndicatorListAPIView.as_view(), name='Indicators'),
    path('category_product/', CategoryProductListAPIView.as_view(), name='Category Products'),
]
