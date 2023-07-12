from rest_framework import generics
from apps.base.api import GenericListAPIView
from apps.products.api.serializers.product_serializer import ProductSerializer
from rest_framework import status
from rest_framework.response import Response


class ProductListAPIView(GenericListAPIView):
    serializer_class = ProductSerializer


class CreateProductAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Producto Creado Satisfactoriamente'
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
