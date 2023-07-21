from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from apps.users.api.serializers import UserTokenSerializer


class Login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data=request.data, context={'request': request}) # EL SERIALIZER TIENE EL PASS Y EL USERNAME
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active:
                token, created = Token.objects.get_or_create(user=user)
                user_serializer = UserTokenSerializer(user)
                if created:
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Bienvenido'
                    }, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Usuario sin acceso'},
                                status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'Nombre de Usuario o Contraseña Inconrrectos'},
                            status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Bienvenido'})

