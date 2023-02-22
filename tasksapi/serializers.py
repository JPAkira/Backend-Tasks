from django.contrib.auth.models import User
from rest_framework import serializers

from tasksapi.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"

    def create(self, validated_data):
        task = Task.objects.create(
            user=self.context['request'].user,
            **validated_data
        )
        return task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password")
