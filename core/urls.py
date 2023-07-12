from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Users/', include('apps.users.api.urls')),
    path('Products/', include('apps.products.api.urls')),
]
