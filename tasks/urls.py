from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tasksapi.views import TaskViewSet

router = routers.SimpleRouter()
router.register(r"tasks", TaskViewSet, basename="tasks")

urlpatterns = [
    path("api/", include(router.urls)),
    path('admin/', admin.site.urls),
]
