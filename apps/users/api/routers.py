from rest_framework.routers import DefaultRouter
from apps.users.api.apiviews import UsersViewSet
from django.urls import path

router = DefaultRouter()

router.register(r'Users', UsersViewSet, basename='users')

urlpatterns = [
    path('Users/Users/<str:username>/', UsersViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='user-detail'),
]


urlpatterns += router.urls
