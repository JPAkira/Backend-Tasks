import django_filters

from tasksapi.models import Task


class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = {
            "name": ["exact", "icontains"],
            "event_at": ["gte", "lte"],
            "finish_at": ["gte", "lte"],
            "priority": ["exact", "in"],
            "status": ["exact", "in"],
        }