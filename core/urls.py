from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from apps.base.views import Login, Logout, UserToken, AuthenticationCodeView


schema_view = get_schema_view(
    openapi.Info(
        title='LOQUEMEVAYUDAR',
        default_version='v1',
        description='LOQUEMEVAYUDAR',
        terms_of_service='https://www.google.com/policies/terms/',
        contact=openapi.Contact(email='penatorresnicolas@gmail.com'),
        license=openapi.License(name='BSD License')
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('login/', Login.as_view(), name='Login'),
    path('verify-code/', AuthenticationCodeView.as_view(), name='verify_code'),
    path('logout/', Logout.as_view(), name='Logout'),
    path('refresh-token/', UserToken.as_view(), name='Refresh Token'),
    path('admin/', admin.site.urls),
    path('Users/', include('apps.users.api.urls')),
    path('Products/', include('apps.products.api.routers')),
    re_path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

