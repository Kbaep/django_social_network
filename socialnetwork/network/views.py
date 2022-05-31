from django.shortcuts import render
from rest_framework import generics, response, views, decorators,status
from .models import Post
from .serializers import PostSerializer
from rest_framework import permissions
from .permissions import IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly


# class PostAPIView(views.APIView):
#     def post(self, request, **kwargs):
#         print('1___________________________')
#         pk = kwargs.get("pk", None)
#         print('1___________________________')
#         if not pk:
#             return response.Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = Post.objects.get(pk=pk)
#         except:
#             return response.Response({"error": "Object does not exists"})
#
#         params: dict = request.json
#         print(params)


class PostAPIListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class PostAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class PostAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly,)


@decorators.api_view(['GET'])
def snippet_list(request, pk, method):
    print(request)
    print(pk)
    print(method)
    print('gyukygukgy1')
    return response.Response(status=status.HTTP_200_OK)