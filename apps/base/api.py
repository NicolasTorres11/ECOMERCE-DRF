from rest_framework import generics
from apps.base.models import BaseModel


class GenericListAPIView(generics.ListAPIView):
    serializer_class = None

    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.filter(state=True)
