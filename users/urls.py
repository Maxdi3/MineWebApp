from django.urls import path

from users.views import UserListAPI

urlpatterns = [
    path('list/', UserListAPI.as_view(), name='users-list')
    ]