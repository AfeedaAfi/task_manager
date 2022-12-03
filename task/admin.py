from django.contrib import admin
from.import models

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'assigned_to', 'assigned_team', 'assigned_by', 'status')
    list_editable = ('status',)

    # def get_queryset(self):
    #     queryset=super(TaskAdmin,self).get_queryset()
    #     models.Task.objects.all()
    #     queryset=queryset.filter(assigned_to=1)
    #     return queryset


admin.site.register(models.Team)
admin.site.register(models.Staff)
# admin.site.register(models.TaskHistory)
admin.site.register(models.Task, TaskAdmin)

