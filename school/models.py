from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    clas = models.ForeignKey("Class", on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=60)
    father_name = models.CharField(max_length=60)
    date_of_birth = models.DateField(null=True)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    county = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class Class(models.Model):
    teacher = models.ManyToManyField(User)
    name = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.name

class File(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    file = models.FileField(blank=True, upload_to='document/')