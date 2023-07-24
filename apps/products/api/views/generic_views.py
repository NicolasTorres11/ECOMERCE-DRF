from apps.base.api import GenericListAPIView
from apps.products.api.serializers.generic_serializers import IndicatorSerializer, CategoryProductSerializer, MeasureUnitSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from apps.products.models import *
from apps.base.authentication.authentication_mixin import Authentication


class MeasureListViewSet(Authentication, viewsets.ReadOnlyModelViewSet):
    """
    hi from measure unit

    """
    model = MeasureUnit
    serializer_class = MeasureUnitSerializer

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.filter(state=True)

    def list(self, request, *args, **kwargs):
        """
        return all measure units

        params.
        name ---------> name

        """
        data = self.get_queryset()
        data = self.serializer_class(data, many=True)
        return Response(data.data, status=status.HTTP_200_OK)

    def create(self):
        return Response({})

    
class IndicatorViewSet(viewsets.ReadOnlyModelViewSet):
    """
    hi from server

    """
    serializer_class = IndicatorSerializer

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.filter(state=True)
    
    def list(self, request, *args, **kwargs):
        data = self.get_queryset()
        data = self.serializer_class(data, many=True)
        return Response(data.data, status=status.HTTP_200_OK)


class CategoryProductViewSet(viewsets.ReadOnlyModelViewSet):
    """
    hi from server

    """
    serializer_class = CategoryProductSerializer

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.filter(state=True)
    
    def list(self, request, *args, **kwargs):
        data = self.get_queryset()
        data = self.serializer_class(data, many=True)
        return Response(data.data, status=status.HTTP_200_OK)

