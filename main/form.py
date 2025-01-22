from django import forms
from .models import Schedule,Note,Task
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class FeedbackModel(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ["subject","day_of_week","time","classroom"]
        labels = {
            "subject":"Предмет",
            "day_of_week":"День недели",
            "time":"Начало пары",
            "classroom": "Комната" 
        }
    def save(self,commit=True,user=None):
        instance = super().save(commit=False)
        if user:
            instance.user = user
        if commit:
            instance.save()
        
        return instance
    

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["content"]
        labels = {
            "content": "Заметка"
        }

    def save(self,commit=True,user=None):
        instance = super().save(commit=False)
        if user:
            instance.user = user
        if commit:
            instance.save()

        return instance

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["subject","task","deadline"]
        labels = {
            "subject":"Предмет",
            "task":"Задания",
            "deadline":"Срок"
            }
    def save(self,commit=True,user=None):
        instance = super().save(commit=False)
        if user:
            instance.user = user
        if commit:
            instance.save()

        return instance

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username","password1","password2")
        labels = {
            "username":"Имя",
            "password1":"Пароль",
            "password2":"Подтверждение пароля"
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя")
    password = forms.CharField(label="Пароль",widget=forms.PasswordInput)