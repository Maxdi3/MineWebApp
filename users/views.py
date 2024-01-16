from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import Users
from users.serializers import UserSerializer
from datetime import datetime, timedelta


class UserListAPI(APIView):

    def get(self, request, *args, **kwargs):
        five_minutes_ago = datetime.now() - timedelta(seconds=15)
        users = Users.objects.filter(last_update__gte=five_minutes_ago)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        try:
            user = Users.objects.get(id=request.data["id"])
        except Users.DoesNotExist:
            return Response({"message": "User not found"}, status=404)

        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            five_minutes_ago = datetime.now() - timedelta(seconds=15)
            m_users = Users.objects.filter(last_update__gte=five_minutes_ago)
            new_serializer = UserSerializer(m_users, many=True)
            return Response(new_serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=400)

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

