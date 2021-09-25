from django.shortcuts import render
from .models import *

def Home(request):
    class_blog = Class_blog.objects.all()
    ticher = Teachers.objects.all()
    gallarey = Gallarey.objects.all()
    context = {
        'class_blog':class_blog,
        'ticher':ticher,
        'gallarey':gallarey,
    }
    return render(request, 'website/Home.html', context)


def Class(request):
    class_blog = Class_blog.objects.all()
    return render(request, 'website/Class.html', {'class_blog':class_blog})


def About(request):
    gallarey = Gallarey.objects.all()
    ticher = Teachers.objects.all()
    context = {
        'ticher':ticher,
        'gallarey':gallarey,
    }
    return render(request, 'website/About.html', context)


def Contact(request):
    return render(request, 'website/Contact.html')


def Enroll_Now(request):
    return render(request, 'website/Enroll_Now.html')
