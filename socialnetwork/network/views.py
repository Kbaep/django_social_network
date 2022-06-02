from rest_framework import decorators, generics, response, status

from .models import Post
from .permissions import IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly
from .serializers import PostSerializer


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
def postrating(request, pk, method):
    if method == 'like':
        Post.objects.filter(pk=pk).update(post_like=Post.objects.get(pk=pk)
                                          .post_like + 1)
    elif method == 'dislike':
        Post.objects.filter(pk=pk).update(post_dislike=Post.objects.get(pk=pk)
                                          .post_dislike + 1)
    return response.Response(status=status.HTTP_200_OK)
