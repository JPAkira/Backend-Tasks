from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

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