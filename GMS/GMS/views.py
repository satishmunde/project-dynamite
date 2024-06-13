from django.http import HttpResponse
from django.shortcuts import render,redirect



def home(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')



def trainers(request):
    return render(request,'trainers.html')



def bloghome(request):
    return render(request,'blog-home.html')



def blogsingle(request):
    return render(request,'blog-single.html')



def schedule(request):
    return render(request,'schedule.html')



def courses(request):
    return render(request,'courses.html')



def contact(request):
    return render(request,'contact.html')


