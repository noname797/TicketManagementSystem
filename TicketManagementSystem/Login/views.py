
from django.shortcuts import render, HttpResponse,redirect

# Create your views here.


def login(request):
    return render(request,'index.html')

def signup(request):
    return render(request,"signup.html")

def reset(request):
    return redirect("/")