from django.shortcuts import render, redirect
from .models import Job, Apply
from .import forms
# Create your views here.
def dash(requset):
    jbs=Job.objects.filter(boy=requset.user)
    for i in jbs:
        global aps
        aps=Apply.objects.filter(job_id=i.id)

        return render(requset,'dahsboard.html',{
            "aps":aps
        })
    return render(requset,"home2.html")










def addjob(request):
    if request.method == "POST":
        form = forms.JobForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.boy = request.user
            instance.save()
            return redirect("/")
    else:
        form = forms.JobForm()
    return render(request, 'addjob.html', {"form": form})


def getJob(request):
    print("job id from get job_______", rp())
    jb=Job.objects.get(pk=int(rp()))
    print("print-------",jb.id)
    if request.method == "POST":
        form = forms.ApplyForm(request.POST , request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.job = jb
            instance.boy= request.user
            instance.save()
            print("passed ")
            return redirect("/")
    else:
        form = forms.ApplyForm()
    return render(request, 'getjob.html',
                  {"form": form},
                  )

def rp():
    print("From rp: ",jid)
    return jid
def detail(request,job_id):
    global jid
    jid=job_id
    job=Job.objects.get(pk=int(job_id))
    print(job.id)
    return render(request, 'detail.html', {'job': job,
                                           })