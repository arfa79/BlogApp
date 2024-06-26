from django.shortcuts import render
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
# Define a viewset for the Post model
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # Apply caching to the dispatch method
    @method_decorator(cache_page(60 * 15)) # Cache page for 15 minutes
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)