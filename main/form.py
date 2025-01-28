from django import forms
from .models import Schedule,Note,Task,Subject,Tag,MyUser,Profile
from django.contrib.auth.forms import UserCreationForm


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
    new_tag = forms.CharField(
        max_length=50,
        required=False,
        label="Добавить новый тэг",
        help_text="Если тэг отсутсвует в списке , добавьте его здесь"
    )

    tag = forms.ModelChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        label="Тэг"
    )
    class Meta:
        model = Note
        fields = ["content","tag"]
        labels = {
            "content": "Заметка"
        }

    def clean(self):
        cleaned_data = super().clean()
        tag = cleaned_data.get("tag")
        new_tag = cleaned_data.get("new_tag")

        if not tag and not new_tag:
            raise forms.ValidationError("Вы должный выбрать существующий тэг или добавить новый")
        
        return cleaned_data
    
    def save(self,commit=True,user=None):
        new_tag = self.cleaned_data.get("new_tag")
        if new_tag:
            tag,created = Tag.objects.get_or_create(name=new_tag)
            self.instance.tag = tag
            
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
    email_address = forms.EmailField(label="Почта",max_length=50,required=True,widget=forms.EmailInput)
    username = forms.CharField(label="Имя пользователя",max_length=50,required=True)
    class Meta:
        model = MyUser
        fields = ["username","email_address","password1","password2"]



class UserForm(forms.Form):
    username = forms.CharField(label="Имя пользователя",max_length=50,required=True)
    email_address = forms.EmailField(label="Почта",max_length=50,required=True,widget=forms.EmailInput)
    password = forms.CharField(label="Пароль",max_length=50,required=True,widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email_address = cleaned_data.get("email_address")
        password = cleaned_data.get("password")
        if not email_address and not password:
            raise forms.ValidationError("Вы должны заполнить все поля")
        
        return cleaned_data
    
class ProfileForm(forms.ModelForm):
    phone = forms.CharField(label="Телефон номер",max_length=50,required=False)
    name = forms.CharField(label="Имя",max_length=50,required=False)
    email = forms.EmailField(label="Почта",max_length=50,required=False)
    city = forms.CharField(label="Город(не обязательно)",max_length=50,required=False)
    country = forms.CharField(label="Страна(не обязательно)",max_length=50,required=False)

    class Meta:
        model = Profile
        fields = ["phone","name","email","city","country"]