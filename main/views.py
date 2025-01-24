from django.shortcuts import render,get_object_or_404,redirect
from .models import Schedule,Note,Task,Subject
from .form import FeedbackModel,NoteForm,TaskForm,SignUpForm,LoginForm
from django.utils import timezone
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def main_menu(request):
    context = Schedule.objects.filter(user=request.user) #* Привязываем к юзеру
    return render(request,'main/index.html',{"context":context})

@login_required
def add_schedule(request):
    if request.method == "POST":
        form = FeedbackModel(request.POST)
        if form.is_valid():
            form.save(user=request.user)
            return redirect("/")
    
    else:
        form = FeedbackModel()

    return render(request,'main/add.html',{"form":form})


def dell_schedule(request,schedule_id):
    if request.method == "POST":
        schedule = get_object_or_404(Schedule,pk=schedule_id)
        schedule.delete()
        return redirect("/")
    


@login_required
def add_notes(request):
    information = Note.objects.filter(user=request.user)
    if request.method == "POST":
        note = NoteForm(request.POST)
        if note.is_valid():
            notes = note.save(commit=False,user=request.user)
            notes.pub_date = timezone.now()
            notes.save()                         
            return redirect("/notes")
    
    else:
        note = NoteForm()

    return render(request,"main/notes.html",{"note":note,"information":information})


def del_notes(request,note_id):
    if request.method == "POST":
        note = get_object_or_404(Note,pk=note_id)
        note.delete()
        return redirect("/notes")
    
@login_required
def add_task(request):
    information = Task.objects.filter(user=request.user)
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save(user=request.user)
            return redirect("/task")
        
    else:
        form = TaskForm()
    
    return render(request,"main/tasks.html",{"form":form,"information":information})

def dell_task(request,task_id):
    if request.method == "POST":
        tasks = get_object_or_404(Task,pk=task_id)
        tasks.delete()
        return redirect("/task")
    


def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect("/")
    else:
        form = SignUpForm()
    return render(request,"main/register.html",{"form":form})

def login_view(request):
    form = LoginForm(data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect("/")
            
    return render(request,"main/login.html",{"form":form})


def profile_view(request):
    name = request.user
    return render(request,"main/profile.html",{"name":name})