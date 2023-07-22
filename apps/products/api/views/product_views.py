from rest_framework import generics
from apps.products.api.serializers.product_serializer import ProductSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from apps.base.authentication.authentication_mixin import Authentication


class ProductViewSet(Authentication, viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    # READ IN VIEWSET
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        else:
            return self.serializer_class().Meta.model.objects.filter(state=True, id=pk).first()

    # LIST IN A VIEWSET

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # CREATE IN VIEWSET

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Producto Creado Exitosamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # UPDATE IN VIEWSET

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE IN VIEWSET

    def destroy(self, request, pk=None):
        product = self.get_queryset().filter(id=pk).first()
        if product:
            product.state = False
            product.save()
            return Response({'message': 'Producto Desactivado'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe este producto'}, status=status.HTTP_404_NOT_FOUND)


# CLASES Y VISTAS TIPIFICADAS CON CADA UN END POINT

# class CreateListProductAPIView(generics.ListCreateAPIView):
#     serializer_class = ProductSerializer
#
#     def get_queryset(self):
#         return self.serializer_class().Meta.model.objects.filter(state=True)
#
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({
#                 'message': 'Producto Creado Satisfactoriamente'
#             }, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class ProductDetailAPIView(generics.RetrieveUpdateAPIView):
#     serializer_class = ProductSerializer
#
#     def get_queryset(self, pk=None):
#         if pk is None:
#             return self.serializer_class().Meta.model.objects.filter(state=True)
#         else:
#             return self.serializer_class().Meta.model.objects.filter(state=True).filter(id=pk).first()
#
#     def delete(self, request, pk=None):
#         product = self.get_queryset(pk)
#         if product:
#             product.state = False
#             product.save()
#             return Response({'message': 'Producto Desactivado'}, status=status.HTTP_200_OK)
#         return Response({'message': 'Producto No encontrado!!!!'}, status=status.HTTP_404_NOT_FOUND)
#
#     def patch(self, request, pk=None):
#
#         if self.get_queryset(pk):
#             product_serializer = self.get_serializer(self.get_queryset(pk))
#             return Response(product_serializer.data, status=status.HTTP_200_OK)
#         return Response({'message': 'Producto No encontrado!!!!'}, status=status.HTTP_404_NOT_FOUND)
#
#     def put(self, request, pk=None):
#         if self.get_queryset(pk):
#             product_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
#             if product_serializer.is_valid():
#                 product_serializer.save()
#                 return Response(product_serializer.data, status=status.HTTP_200_OK)
#             return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class DestroyProductAPIView(generics.DestroyAPIView):
#     serializer_class = ProductSerializer
#
#     def get_queryset(self):
#         model = self.serializer_class().Meta.model
#         return model.objects.filter(state=True)
#
#     def delete(self, request, pk=None):
#         product = self.get_queryset().filter(id=pk).first()
#         if product:
#             product.state = False
#             product.save()
#             return Response({'message': 'Producto Desactivado'}, status=status.HTTP_200_OK)
#         return Response({'message': 'Producto No encontrado!!!!'}, status=status.HTTP_404_NOT_FOUND)
#
#
# class ProductUpdateAPIView(generics.UpdateAPIView):
#     serializer_class = ProductSerializer
#
#     def get_queryset(self, pk=None):
#         return self.serializer_class().Meta.model.objects.filter(state=True).filter(id=pk).first()
#
#     def patch(self, request, pk=None):
#
#         if self.get_queryset(pk):
#             product_serializer = self.get_serializer(self.get_queryset(pk))
#             return Response(product_serializer.data, status=status.HTTP_200_OK)
#         return Response({'message': 'Producto No encontrado!!!!'}, status=status.HTTP_404_NOT_FOUND)
#
#     def put(self, request, pk=None):
#         if self.get_queryset(pk):
#             product_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
#             if product_serializer.is_valid():
#                 product_serializer.save()
#                 return Response(product_serializer.data, status=status.HTTP_200_OK)
#             return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)




