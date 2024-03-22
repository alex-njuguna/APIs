from rest_framework import serializers

from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    # convert the Todo model data to json
    class Meta:
        model = Todo
        fields = ['id', 'title', 'body']
        