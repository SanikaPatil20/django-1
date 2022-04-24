from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return HttpResponse("this is our Project")
def Homepage(request):
    #return HttpResponse("This is new ome hoempage")
    return render(request,'Homepage.html')
def Login(request):
    return render(request,'Login.html')
def AboutUS(request):
    return render(request,'AboutUs.html')
def ContactUs(request):
    return render(request,'ContactUs.html')

def Takeattendance(request):
    return render(request,'Takeattendance.html')

def studentpage(request):
    return render(request,'studentpage.html')
def TeacherLogin(request):
    return render(request,'TeacherLogin.html')
def StudentLogin(request):
    return render(request,'StudentLogin.html')
def AdminPage(request):
    return render(request,'AdminPage.html')
def AddStudent(request):
    return render(request,'AddStudent.html')