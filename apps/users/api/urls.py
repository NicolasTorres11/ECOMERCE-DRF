from django.urls import path
from .apiviews import user_api_view, user_detail_view

urlpatterns = [
    path('users/', user_api_view, name='users'),
    path('users_detail/<int:username>', user_detail_view, name='users_detail')
]