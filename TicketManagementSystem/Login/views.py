
from multiprocessing import context
from django.shortcuts import render, HttpResponse,redirect
from Login.models import Profile
from django.contrib import messages
from django.http import HttpResponseRedirect
from rest_framework import generics, permissions
from rest_framework.response import Response
# from knox.models import AuthToken
# from .serializers import UserSerializer, RegisterSerializer

# Create your views here.


def login(request):
    return render(request,'index.html')

def signup(request):
    if request.method == 'POST':
        psno = request.POST.get('psno')
        name = request.POST.get('name')
        email = request.POST.get('email')

        password = request.POST.get('password')
        # confirmpassword = request.POST.get('confirmpassword')

        print(request.POST.get('psno'))

        user_obj = Profile.objects.filter(ps_number = psno)

        if user_obj.exists():
            mes ='User with this PS Number already Exists.'
            context ={
                'error' : mes,
            }
            return render(request,'signup.html',context)
        
        try:
            user_obj = Profile.objects.create(ps_number=psno,name=name,email=email,password=password)
            print(user_obj)
            user_obj.save()
            messages.success(request,'Account has been created successfully. You can now Login into TMS.')
            return redirect('/')
        except Exception as e:
            print(e)
            
            messages.warning(request, 'There is some problem with the account registeration.Please contact the admin.')
    return render(request,'signup.html',)

def reset(request):
    return redirect("/")