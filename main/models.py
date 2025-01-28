from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    email_address = models.EmailField(unique=True,max_length=50)
    USERNAME_FIELD = "email_address"
    username = models.CharField(max_length=100,blank=True,null=True)
    REQUIRED_FIELDS = ["username"]
    
    def __str__(self):
        return self.email_address

class Subject(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Schedule(models.Model):
    DAYS_OF_WEEK = [
        ("MON","Понедельник"),
        ("TUE","Вторник"),
        ("WED","Среда"),
        ("THU","Четверг"),
        ("FRI","Пятница"),
        ("SAT","Суббота"),
        ("SUN","Воскресенье")
    ]
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE) #* Привязываем к пользователю
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE,related_name="schedule")
    classroom = models.IntegerField(verbose_name="Номер комнаты")
    day_of_week = models.CharField(max_length=3,choices=DAYS_OF_WEEK,verbose_name="День недели")
    time = models.CharField(verbose_name="Начало занятии")
    
    def __str__(self):
        return f"{self.subject} ({self.day_of_week} - {self.time})"
    

class Note(models.Model):
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    content = models.CharField()
    pub_date = models.DateTimeField()
    tag = models.ForeignKey(Tag,on_delete=models.CASCADE)


class Task(models.Model):
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    task = models.CharField()
    deadline = models.CharField()
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE,related_name="tasks")


