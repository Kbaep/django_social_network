from django.shortcuts import render
from rest_framework import generics, response,views
from .models import Post
from .serializers import PostSerializer


class PostAPIView(views.APIView):
    def post(self, request, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return response.Response({"error": "Method PUT not allowed"})

        try:
            instance = Post.objects.get(pk=pk)
        except:
            return response.Response({"error": "Object does not exists"})

        params: dict = request.json
        print(params)

class PostAPIListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

