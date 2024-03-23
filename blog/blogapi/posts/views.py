from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Post
from .serializers import PostSerializer

class PostList(ListCreateAPIView):
    # display a collectioon of posts as well as allow creating new ones
    queryset = Post.objects.all()
    serializer_class = PostSerializer
