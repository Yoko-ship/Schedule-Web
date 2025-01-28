from django.shortcuts import render,get_object_or_404,redirect
from .models import Schedule,Note,Task,Profile
from .form import FeedbackModel,NoteForm,TaskForm,SignUpForm,UserForm,ProfileForm
from django.utils import timezone
from django.contrib.auth import login,authenticate
from django.views.generic import TemplateView,View
from django.contrib.auth.mixins import LoginRequiredMixin


class Login_Required(LoginRequiredMixin):
    login_url = "/login"
    redirect_field_name = "/"

class MainView(Login_Required,TemplateView):
    template_name = "main/index.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["context"] = Schedule.objects.filter(user=self.request.user)
        return context
    
class AddSchedule(Login_Required,View):
    form_class = FeedbackModel
    template_name = "main/add.html"

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(user=self.request.user)
            return redirect("/")
        return render(request,self.template_name,{"form":form})
    
    def get(self,request,*args,**kwargs):
        form = self.form_class
        return render(request,self.template_name,{"form":form})
    
class DellView(View):
    def post(self,request,schedule_id,*args,**kwargs):
            schedule = get_object_or_404(Schedule,pk=schedule_id)
            schedule.delete()
            return redirect("/")
    



class AddNotes(Login_Required,TemplateView):
    template_name = "main/notes.html"

    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["information"] = Note.objects.filter(user=self.request.user)
        return context        

    def get(self,request):
        form = NoteForm()
        return render(request,self.template_name,{"note":form,**self.get_context_data()})    


    def post(self,request,):
        form = NoteForm(request.POST)
        if form.is_valid():
            notes = form.save(commit=False,user=request.user)
            notes.pub_date = timezone.now()
            notes.save()
            return redirect("/notes")
        return render(request,self.template_name,{"note":form,**self.get_context_data()})
    

class DellNotes(View):
    def post(self,request,note_id,*args,**kwargs):
        note = get_object_or_404(Note,pk=note_id)
        note.delete()
        return redirect("/notes")
    

class AddTask(Login_Required,TemplateView):
    template_name = "main/tasks.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["information"] = Task.objects.filter(user=self.request.user)
        return context
    
    def post(self,request,*args):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save(user=request.user)
            return redirect("/task")
        return render(request,self.template_name,{"form":form,**self.get_context_data()})
    
    def get(self,request,*args):
        form = TaskForm()
        return render(request,self.template_name,{"form":form,**self.get_context_data()})
    

class DellTask(View):
    def post(self,request,task_id):
        tasks = get_object_or_404(Task,pk=task_id)
        tasks.delete()
        return redirect("/task")




class Register(View):
    form_class = SignUpForm
    template_name = "main/register.html"
    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect("/update_profile")
        return render(request,self.template_name,{"form":form})
    def get(self,request,*args,**kwargs):
        form = self.form_class()
        return render(request,self.template_name,{"form":form})

class LoginView(View):
    template_name = "main/login.html"
    def post(self,request,*args):
        form = UserForm(data=request.POST or None)
        if form.is_valid():
            email_address = form.cleaned_data.get("email_address")
            password = form.cleaned_data.get("password")
            user = authenticate(email_address=email_address,password=password)
            if user is not None:
                login(request,user)
                return redirect("/")
            
        return render(request,self.template_name,{"form":form})

    def get(self,request,*args):
        form = UserForm()
        return render(request,self.template_name,{"form":form})
    

class ProfileView(TemplateView):
    model = Profile
    template_name = "main/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['information'] = Profile.objects.get_or_create(user=self.request.user)
        return context


def update_profile(request):
    if request.user.is_authenticated:
        current_user,created = Profile.objects.get_or_create(user=request.user)
        form = ProfileForm(request.POST or None,instance=current_user)
        if form.is_valid():
            form.save()
            return redirect("/profile")
    
        return render(request,"main/update_profile.html",{"form":form})
    else:
        return redirect("/login")
        