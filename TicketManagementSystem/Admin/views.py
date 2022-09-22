from django.shortcuts import render

# Create your views here.


def alltickets(request):
    return render(request,"alltickets.html")