from django.contrib import admin
from .models import Task
# Register your models here.


@admin.register(Task)
class tasks(admin.ModelAdmin):
    list_display = ('title', 'completed', 'created_at', 'due_date')
    search_fields = ('completed', 'created_at')