from django import forms
from .models import Schedule,Note,Task,Subject
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class FeedbackModel(forms.ModelForm):
    new_subject = forms.CharField(
        max_length=200,
        required=False,
        label="Добавить новый предмет",
        help_text="Если предмет отсутствует в списке , добавьте его здесь"
    )

    subject = forms.ModelChoiceField(
        queryset=Subject.objects.all(),
        required=False,
        widget=forms.Select(attrs={"class":"form-control"}),
        label="Предмет"
    )

    class Meta:
        model = Schedule
        fields = ["subject","new_subject","day_of_week","time","classroom"]
        labels = {
            "day_of_week":"День недели",
            "time":"Начало пары",
            "classroom": "Комната" 
        }

    def clean(self):
        cleaned_data = super().clean()
        subject = cleaned_data.get("subject")
        new_subject = cleaned_data.get("new_subject")

        if not subject and not new_subject:
            raise forms.ValidationError("Вы должны выбрать существующий предмет или добавить новый")
        
        if not subject and new_subject:
            cleaned_data["subject"] = Subject.objects.create(name=new_subject)
    
        return cleaned_data

    
    def save(self,commit=True,user=None):
        new_subject = self.cleaned_data.get("new_subject")
        if new_subject:
            subject,created = Subject.objects.get_or_create(name=new_subject)
            self.instance.subject = subject

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
    new_subject = forms.CharField(
        max_length=200,
        required=False,
        label="Добавить новый предмет",
        help_text="Если предмет отсутствует в списке,добавьте его здесь"
    )

    subject = forms.ModelChoiceField(
        queryset=Subject.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class':"form-control"}),
        label="Предмет"
    )

    class Meta:
        model = Task
        fields = ["task","deadline","subject","new_subject"]
        
        labels = {
            "task":"Задания",
            "deadline":"Срок"
            }
        

    def clean(self):
        cleaned_data = super().clean()
        subject = cleaned_data.get("subject")
        new_subject = cleaned_data.get("new_subject")

        if not subject and not new_subject:
            raise forms.ValidationError("Вы должны выбрать существующий предмет либо добавить новый")
        
        return cleaned_data

    def save(self,commit=True,user=None):
        new_subject = self.cleaned_data.get("new_subject")
        if new_subject:
            subject,created = Subject.objects.get_or_create(name=new_subject)
            self.instance.subject = subject

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