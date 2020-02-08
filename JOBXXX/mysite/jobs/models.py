from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Job(models.Model):
    name=models.CharField(max_length=500, default='Job Tittle')
    description=models.CharField(max_length=500, default='Job Description')
    phone=models.CharField(max_length=500, default='01715254640')
    salary=models.FloatField( default=0.0)
    boy = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

class Apply(models.Model):
    name=models.CharField(max_length=100, default="Your Name")
    mail=models.EmailField(max_length=100)
    phone=models.CharField(max_length=500, default='01000000000')
    job=models.ForeignKey(Job, default=None,on_delete=models.CASCADE)
    cv =models.FileField(upload_to='cv', default='cv.txt')
    student_id =models.FileField(upload_to='id', blank=False, null=False )
    boy = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

