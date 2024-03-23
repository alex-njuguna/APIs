from rest_framework import serializers

from .models import Post

class PostSerializer(serializers.ModelSerializer):
    # convert the Post model to json
    model = Post
    fields = ['id', 'author', 'title', 'body', 'created_at']
