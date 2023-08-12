from app.models import TaskItem
from rest_framework import serializers


class TaskItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskItem
        fields = '__all__'