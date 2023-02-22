from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tasksapi.views import TaskViewSet, UserViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = routers.SimpleRouter()
router.register(r"tasks", TaskViewSet, basename="tasks")
router.register(r"users", UserViewSet, basename="users")

urlpatterns = [
    path("backend/api/", include(router.urls)),
    path('backend/admin/', admin.site.urls),
    path('backend/api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('backend/api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
