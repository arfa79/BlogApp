from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
# Define a viewset for the Post model
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all() # Queryset containing all Post objects
    serializer_class = PostSerializer # Serializer class for Post objects