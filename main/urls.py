from django.urls import path,include
from . import views



urlpatterns = [
    path("",views.main_menu,name="menu"),
    path("add/",views.add_schedule,name="add"),
    path("delete/<int:schedule_id>/",views.dell_schedule,name="delete"),
    path("notes/",views.add_notes,name="add_notes"),
    path("task/",views.add_task,name="task"),
    path("notes/dell/<int:note_id>/",views.del_notes,name="del_notes"),
    path("task/dell/<int:task_id>/",views.dell_task,name="dell_task"),
    path("accounts/",include("django.contrib.auth.urls")),
    path("profile/",views.profile_view,name="profile"),
    path("register/",views.register,name="register"),
    path("login/",views.login_view,name="login_view"),
]
