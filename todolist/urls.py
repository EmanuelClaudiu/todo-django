from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import TaskItemViewset, ProjectViewset

app_name = "todo"

router = DefaultRouter()
router.register(r"taskitem", TaskItemViewset)
router.register(r"project", ProjectViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('', views.list_tasks, name="list_tasks")
]