from rest_framework import generics, status
from rest_framework.response import Response
from apps.products.api.serializers.product_serializers import ProductSerializer
from apps.base.api import GeneralListAPIView


class ListCreateProductAPIView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = serializer_class.Meta.model.objects.filter(state=True)
    # SOBRE ESCRIBIR UN METODO POST

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Producto Creado Correctamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()

    def patch(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk))
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'error': 'No existe este Producto'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        product = self.get_queryset(pk)
        if product:
            product.state = False
            product.save()
            return Response({'message': 'Producto Desactivado Correctamente'}, status=status.HTTP_200_OK)
        return Response({'message': 'No existe este Producto'}, status=status.HTTP_400_BAD_REQUEST)

# class ProductDeleteAPIView(generics.DestroyAPIView):
#     serializer_class = ProductSerializer
#
#     def get_queryset(self):
#         return self.get_serializer().Meta.model.objects.filter(state=True)
#
#     def delete(self, request, pk=None):
#         product = self.get_queryset().filter(id=pk).first()
#         if product:
#             product.state = False
#             product.save()
#             return Response({'message': 'Producto Desactivado Correctamente'}, status=status.HTTP_200_OK)
#         return Response({'message': 'No existe este Producto'}, status=status.HTTP_400_BAD_REQUEST)
#
#
# class ProductUpdateAPIView(generics.UpdateAPIView):
#     serializer_class = ProductSerializer
#
#     def get_queryset(self, pk):
#         return self.get_serializer().Meta.model.objects.filter(state=True).filter(id=pk).first()
#
#     def patch(self, request, pk=None):
#         if self.get_queryset(pk):
#             serializer = self.serializer_class(self.get_queryset(pk))
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response({'error': 'No existe este Producto'}, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request, pk=None):
#         if self.get_queryset(pk):
#             serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
