from django.shortcuts import render
from jobs.models import Job

def home(request):
    jobs=Job.objects.all()
    return render(request,'home.html',{
        "job":jobs
    })


def about(request):
    return render(request,'about.html')
