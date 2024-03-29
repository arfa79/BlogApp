from rest_framework import serializers
from .models import Post
# Define a serializer for the Post model
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__' # Serialize all fields of the model