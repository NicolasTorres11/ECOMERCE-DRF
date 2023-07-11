from rest_framework import status
from rest_framework.decorators import api_view
from apps.users.models import User
from .serializers import UserSerializer, UserListSerializer
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def user_api_view(request):

    # LIST
    if request.method == 'GET':
        # QUERYSET
        users = User.objects.filter(is_active=True).values('id', 'username', 'password', 'name', 'email')
        serializer = UserListSerializer(users, many=True)
        # test_data = {
        #     'username': 14789,
        #     'name': 'nicolas',
        #     'email': '107480@gmail.com',
        # }
        # test_user = TestUserSerializer(data=test_data, context=test_data)
        # if test_user.is_valid():
        #     user_instance = test_user.save()
        #     print(user_instance)
        # else:
        #     print(test_user.errors)
        return Response(serializer.data, status=status.HTTP_200_OK)
    # CREATE
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)

        # VALIDATION OF CREATE
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Usuario Creado Correctamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_view(request, username):

    # QUERY SET CONSULT
    users = User.objects.filter(username=username).first()

    # VALIDATE QUERYSET
    if users:
        # RETRIEVE
        if request.method == 'GET':
            serializer = UserSerializer(users)
            return Response(serializer.data, status=status.HTTP_200_OK)
        # UPDATE
        elif request.method == 'PUT':
            serializer = UserSerializer(users, data=request.data)
            if serializer.is_valid():
                serializer.is_active = False
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # DELETE OR DEACTIVATED
        elif request.method == 'DELETE':
            # user = User.objects.filter(username=username).first()
            # user.delete()
            # return Response('Object Deleted')
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            user.is_active = False
            user.save()
            return Response({
                'message': 'Usuario Desactivado?'
            }, status=status.HTTP_202_ACCEPTED)
    return Response({'message': 'No se ha encontrado el Usuario'}, status=status.HTTP_400_BAD_REQUEST)







