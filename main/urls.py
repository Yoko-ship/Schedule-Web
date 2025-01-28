from django.urls import path,include
from . import views



urlpatterns = [
    path("",views.MainView.as_view(),name="menu"),
    path("add/",views.AddSchedule.as_view(),name="add"),
    path("delete/<int:schedule_id>/",views.DellView.as_view(),name="delete"),
    path("notes/",views.AddNotes.as_view(),name="add_notes"),
    path("task/",views.AddTask.as_view(),name="task"),
    path("notes/dell/<int:note_id>/",views.DellNotes.as_view(),name="del_notes"),
    path("task/dell/<int:task_id>/",views.DellTask.as_view(),name="dell_task"),
    path("accounts/",include("django.contrib.auth.urls")),
    path("profile/",views.ProfileView.as_view(),name="profile"),
    path("register/",views.Register.as_view(),name="register"),
    path("login/",views.LoginView.as_view(),name="login_view"),
    path("update_profile/",views.update_profile,name="update_profile")
]
