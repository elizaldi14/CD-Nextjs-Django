from rest_framework import serializers
from .models import Task

# En esta clase convierte instancias del modelo Task a respresentacion JSON

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'done', 'created_at')
        read_only_fields = ('id', 'created_at')
