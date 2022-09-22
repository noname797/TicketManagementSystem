from django.shortcuts import render

# Create your views here.


def alltickets(request):
    return render(request,"alltickets.html")

def dashboard(request):
    return render(request,"dashboard.html")

def reset(request):
    return redirect("/")