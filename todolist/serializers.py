from rest_framework import serializers

from todolist.models import TaskItem, Project


class TaskItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskItem
        fields = ("id", "title", "due_date", "creation_date", "description", "owner",
                  "project", "last_updated_date", "status")

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("name", "owner", "task_count")

    task_count = serializers.SerializerMethodField()

    def get_task_count(self, instance):
        return TaskItem.objects.filter(project=instance).count()
