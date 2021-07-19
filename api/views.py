from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import UserSerializer


# Create your views here.
class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass
