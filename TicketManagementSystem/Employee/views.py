from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

def raiseReq(request):
    return render(request,"raiseReq.html")

def reset(request):
    return redirect("/")

def user_history(request):
    return render(request,"history.html")