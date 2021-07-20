from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from post.models import Post
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import PostSerializer


# Create your views here.
class PostListAPIView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
class PostDetailAPIView(APIView):
    def get(self, request, pk=None):
        posts = Post.objects.all()
        post = get_object_or_404(posts, pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
