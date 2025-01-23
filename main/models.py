from django.db import models
from django.contrib.auth.models import User

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
    user = models.ForeignKey(User,on_delete=models.CASCADE) #* Привязываем к пользователю
    subject = models.CharField(max_length=50,verbose_name="Названия предмета")
    classroom = models.IntegerField(verbose_name="Номер комнаты")
    day_of_week = models.CharField(max_length=3,choices=DAYS_OF_WEEK,verbose_name="День недели")
    time = models.CharField(verbose_name="Начало занятии")
    
    def __str__(self):
        return f"{self.subject} ({self.day_of_week} - {self.time})"
    

class Note(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.CharField()
    pub_date = models.DateTimeField()


class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.CharField()
    task = models.CharField()
    deadline = models.CharField()

