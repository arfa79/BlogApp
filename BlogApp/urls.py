from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.views import PostViewSet
from rest_framework.authtoken.views import ObtainAuthToken
router = DefaultRouter()
router.register(r'posts', PostViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls), 
    path('api-token-auth/', ObtainAuthToken.as_view(), name='api_token_auth'),
]
