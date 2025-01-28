from django.contrib import admin
from .models import Schedule,Note,Task,Subject,Tag,MyUser,Profile
class AdminCustom(admin.ModelAdmin):
    list_display = ["subject","day_of_week","time","classroom"]

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
admin.site.register(Tag)
admin.site.register(MyUser)
admin.site.register(Profile)
