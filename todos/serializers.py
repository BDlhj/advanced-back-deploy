from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Todo
    fields = ['text', 'done', 'author', 'created_at', 'updated_at']
