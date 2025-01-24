from django.contrib import admin
from .models import Schedule,Note,Task,Subject
class AdminCustom(admin.ModelAdmin):
    # fieldsets = [
    #     ("Занятия",{"fields": ["lesson"]}),
    #     ("День",{"fields":["day"]}),
    #     ("Время",{"fields":["time"]})
    # ]

    list_display = ["subject","day_of_week","time","classroom"]
    # search_fields = ["day"]

class TaskInline(admin.TabularInline):
    model = Task
class TaskAdmin(admin.ModelAdmin):
    inlines = [
        TaskInline,
    ]

admin.site.register(Schedule,AdminCustom)
admin.site.register(Note)
admin.site.register(Task)
admin.site.register(Subject,TaskAdmin)
