from django.contrib.auth.models import User
from django.db import models

class TaskItem(models.Model):
    NEW = 1
    IN_PROGRESS = 2
    DONE = 3

    STATUSES = [(NEW, "New"),
                (IN_PROGRESS, "In progress"),
                (DONE, "Done")]

    title = models.CharField(max_length=1024)
    description = models.CharField(max_length=1024, blank=True, null=True)

    due_date = models.DateTimeField()
    creation_date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    status = models.IntegerField(choices=STATUSES, default=NEW)

    cost = models.IntegerField(default=0)

    project = models.ForeignKey("todolist.Project", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

class Project(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.name