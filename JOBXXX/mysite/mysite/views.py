from django.shortcuts import render,redirect
from jobs.models import Job
from django.core.mail import send_mail


def home(request):
    jobs=Job.objects.all()
    return render(request,'home.html',{
        "job":jobs
    })


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request, 'contact.html')

def sendInfo(request):
    if request.method == "GET":
        fname = request.GET['fname']
        lname = request.GET['lname']
        email = request.GET['email']
        comment = request.GET['comment']
        print(fname)
        print(lname)
        print(email)
        print(comment)

        return redirect("/")

def sendemail(request):
    if request.method == "GET":
        fname = request.GET['fname']
        lname = request.GET['lname']
        email = request.GET['email']
        comment = request.GET['comment']

        str000 = "Name : "
        str0 = fname + " " + lname + " "
        str00 = "\n"
        str = email
        str3 = "Sent by :"
        str4 = "\n"
        str2 = comment
        str5 = "Feedback: "

    send_mail(fname, str000 + str0 + str00 + str3 + str + str4 + str5 + str2, email, ['rayhan.rohan10@gmail.com'])
    fail_silently = False
    return render(request, 'contact2.html')