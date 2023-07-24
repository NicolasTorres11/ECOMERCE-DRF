from rest_framework import serializers
from apps.base.models import Code


class CodeSerializer(serializers.ModelSerializer):
    number = serializers.CharField(label='Code', help_text='Ingrese el mensaje de texto que llego a su telefono')

    class Meta:
        model = Code
        fields = '__all__'
