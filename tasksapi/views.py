from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from tasksapi import serializers
from tasksapi.filters import TaskFilter
from tasksapi.models import Task
from django_filters import rest_framework as filters


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = serializers.TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TaskFilter

