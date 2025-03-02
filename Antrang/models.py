from django.db import models

# Create your models here.

class Dept(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Course(models.Model):
    name = models.CharField(max_length=100)
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
    
    

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact =models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)
    def __str__(self):
        return self.name 


class Event(models.Model):
    name=models.CharField(max_length=100)
    date_time=models.DateTimeField()
    venue=models.TextField()
    created_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
class Parti(models.Model):
    name=models.CharField(max_length=100)
    event=models.ForeignKey(Event, on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
    