from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

def ticket_request(request):
    return render(request,"ticketRequest.html")

def reset(request):
    return redirect("/")