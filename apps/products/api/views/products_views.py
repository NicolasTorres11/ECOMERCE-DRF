from rest_framework import generics, status
from rest_framework.response import Response
from apps.products.api.serializers.product_serializers import ProductSerializer
from apps.base.api import GeneralListAPIView


class ProductListAPIView(GeneralListAPIView):
    serializer_class = ProductSerializer


class CreateProductAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer

    # SOBRE ESCRIBIR UN METODO POST

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Producto Creado Correctamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


