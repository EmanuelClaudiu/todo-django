from django.contrib import admin

# Register your models here.
from todolist.models import TaskItem, Project

class TaskItemAdmin(admin.ModelAdmin):
    list_display = ["title", "due_date", "creation_date", "description", "project", "status"]
    list_filter = ["project", "owner"]
    search_fields = ["title"]

class ProjectAdmin(admin.ModelAdmin):
    exclude = ["owner"]

admin.site.register(TaskItem, TaskItemAdmin)
admin.site.register(Project)