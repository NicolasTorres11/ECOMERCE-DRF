import random
from rest_framework.views import APIView
from django.contrib.sessions.models import Session
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from rest_framework.authtoken.models import Token
from apps.base.models import Code
from apps.users.api.serializers import UserTokenSerializer
from django.conf import settings
from twilio.rest import Client


class UserToken(APIView):
    def get(self, request, *args, **kwargs):
        username = request.GET.get('username')
        try:
            user_token = Token.objects.get(user=UserTokenSerializer().Meta.model.objects.filter(username=username).first())
            return Response({
                'token': user_token.key
            }, status=status.HTTP_200_OK)
        except:
            return Response({
                'error': 'Credenciales Incorrectas'
            }, status=status.HTTP_401_UNAUTHORIZED)


class Login(ObtainAuthToken):

    def generate_verification_code(self, user):
        verification_code = str(random.randint(100000, 999999))
        code_obj, created = Code.objects.get_or_create(user=user)
        code_obj.code = verification_code
        code_obj.save()

        return verification_code

    def send_verification_code(self, phone_number, code):
        account_sid = settings.TWILIO_ACCOUNT_SID
        auth_token = settings.TWILIO_AUTH_TOKEN
        twilio_phone_number = settings.TWILIO_PHONE_NUMBER

        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=f'Tu código de verificación es: {code}',
            from_=twilio_phone_number,
            to=str(phone_number)
        )

    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data=request.data, context={'request': request}) # EL SERIALIZER TIENE EL PASS Y EL USERNAME
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active:
                verification_code = self.generate_verification_code(user)
                phone_number = '+573053218312'
                self.send_verification_code(phone_number, verification_code)
                return Response({
                    'message': 'Código de verificación enviado al usuario. Por favor, '
                               'ingresa el código para completar el inicio de sesión.',
                }, status=status.HTTP_200_OK)
            else:
                    return Response({'error': 'Usuario sin acceso'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'Nombre de Usuario o Contraseña Incorrectos'}, status=status.HTTP_400_BAD_REQUEST)


class AuthenticationCodeView(APIView):
    def post(self, request, *args, **kwargs):
        # Recuperar el código de autenticación ingresado por el usuario
        authentication_code = request.data.get('authentication_code')

        # Obtener el usuario relacionado con el código de autenticación (puedes usar tu lógica de búsqueda)
        try:
            user = Code.objects.get(code=authentication_code).user
        except Code.DoesNotExist:
            return Response({'error': 'Código de autenticación inválido.'}, status=status.HTTP_404_NOT_FOUND)

        if user.is_active:
            token, created = Token.objects.get_or_create(user=user)
            user_serializer = UserTokenSerializer(user)
            if created:
                return Response({
                    'token': token.key,
                    'user': user_serializer.data,
                    'message': 'Inicio de Sesion Exitoso.',
                }, status=status.HTTP_201_CREATED)
            else:
                all_sessions = Session.objects.filter(expire_date__gte=datetime.now())
                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get('_auth_user_id')):
                            session.delete()
                token.delete()
                token = Token.objects.create(user=user)
                return Response({
                    'token': token.key,
                    'user': user_serializer.data,
                    'message': 'Inicio de Sesion Exitoso.',
                })
        else:
            return Response({'error': 'Usuario sin acceso'}, status=status.HTTP_401_UNAUTHORIZED)


class Logout(APIView):
    def get(self, request, *args, **kwargs):
        try:
            token = Token.objects.filter(key=request.GET.get('token')).first()
            if token:
                user = token.user
                all_session = Session.objects.filter(expire_date__gte=datetime.now())
                if all_session.exists():
                    for session in all_session:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get('_auth_user_id')):
                            session.delete()
                token.delete()

                session_message = 'Sesiones Eliminadas.'
                token_messages = 'Token eliminado.'
                return Response({
                    'token_message': token_messages,
                    'session_message': session_message
                }, status=status.HTTP_200_OK)
            return Response({
                'error': 'No se ha Encontrado un Usuario con estas credenciales'
            }, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({
                'error': 'No existe un token en esta peticion'
            }, status=status.HTTP_409_CONFLICT)







# class Login(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         login_serializer = self.serializer_class(data=request.data, context={'request': request}) # EL SERIALIZER TIENE EL PASS Y EL USERNAME
#         if login_serializer.is_valid():
#             user = login_serializer.validated_data['user']
#             if user.is_active:
#                 token, created = Token.objects.get_or_create(user=user)
#                 user_serializer = UserTokenSerializer(user)
#                 if created:
#                     return Response({
#                         'token': token.key,
#                         'user': user_serializer.data,
#                         'message': 'Inicio de Sesion Exitoso.',
#                     }, status=status.HTTP_201_CREATED)
#                 else:
#                     all_sessions = Session.objects.filter(expire_date__gte=datetime.now())
#                     if all_sessions.exists():
#                         for session in all_sessions:
#                             session_data = session.get_decoded()
#                             if user.id == int(session_data.get('_auth_user_id')):
#                                 session.delete()
#                     token.delete()
#                     token = Token.objects.create(user=user)
#                     return Response({
#                         'token': token.key,
#                         'user': user_serializer.data,
#                         'message': 'Inicio de Sesion Exitoso.',
#                     })
#             else:
#                 return Response({'error': 'Usuario sin acceso'},
#                                 status=status.HTTP_401_UNAUTHORIZED)
#         else:
#             return Response({'error': 'Nombre de Usuario o Contraseña Inconrrectos'},
#                             status=status.HTTP_400_BAD_REQUEST)


# class Login2(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         login_serializer = self.serializer_class(data=request.data, context={'request': request}) # EL SERIALIZER TIENE EL PASS Y EL USERNAME
#         if login_serializer.is_valid():
#             user = login_serializer.validated_data['user']
#             if user.is_active:
#                 token, created = Token.objects.get_or_create(user=user)
#                 user_serializer = UserTokenSerializer(user)
#                 if created:
#                     return Response({
#                         'token': token.key,
#                         'user': user_serializer.data,
#                         'message': 'Inicio de Sesion Exitoso.',
#                     }, status=status.HTTP_201_CREATED)
#                 else:
#                     token.delete()
#                     return Response({'error': 'No Puedes Iniciar session con esta cuenta'}, status=status.HTTP_409_CONFLICT)
#             else:
#                 return Response({'error': 'Usuario sin acceso'},
#                                 status=status.HTTP_401_UNAUTHORIZED)
#         else:
#             return Response({'error': 'Nombre de Usuario o Contraseña Inconrrectos'},
#                             status=status.HTTP_400_BAD_REQUEST)




