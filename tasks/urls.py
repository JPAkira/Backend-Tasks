from django.contrib import admin
from django.urls import path
from rest_framework import routers
from tasksapi.views import TaskViewSet

router = routers.SimpleRouter()
router.register(r"api/tasks", TaskViewSet, basename="tasks")

urlpatterns = [
    path('admin/', admin.site.urls),
]
