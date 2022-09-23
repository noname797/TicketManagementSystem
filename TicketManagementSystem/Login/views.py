
from functools import partial
import profile
from urllib import response
from django.shortcuts import render, HttpResponse,redirect
from rest_framework import viewsets
from .serializers import ProfileSerializer
from .models import Profile
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
from Employee import *
from rest_framework.parsers import JSONParser 
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
# Create your views here.


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class RegisterView(APIView):
    def post(self, request):
        print(request.data)
        data_e={}
        data_e['password']=make_password(request.data['password'])
        data_e['ps_number']=request.data['ps_number']
        data_e['email']=request.data['email']
        data_e['name']=request.data['name']
        serializer = ProfileSerializer(data=data_e)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            #print("hi")
            #return render(request,"index.html")
        except:
        #     mes ='User with this PS Number already Exists.'
        #     context ={
        #         'error' : mes,
        #     }
        #    return render(request,'signup.html',context)
            return Response(serializer.errors)

class LoginView(APIView):
    def post(self, request):
        ps_number = request.data['username']
        pas= request.data['password']

        #try:
        user = Profile.objects.filter(ps_number=ps_number).first()
        # print("user",user.password)
        
        if user is None:
            # raise AuthenticationFailed("User not found")
            response=Response()
            response.data={
                'detail':"User not found"
            }
            return response
        # if pas!=user.password:
        if not check_password(pas, user.password):
            print("pass incorrect")
            # raise AuthenticationFailed('Incorrect password!')
            response=Response()
            response.data={
                'detail':"Incorrect password!"
            }
            return response

        request.session['user_id'] = user.id
        request.session['role_id'] = 1 if user.is_admin else 0
        print(request.session)
        response=Response()
        response.data={
            'id':user.id,
            'is_admin':user.is_admin,
        }
        return response

            # payload = {
            #     'id': user.ps_number,
            #     'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            #     'iat': datetime.datetime.utcnow()
            # }
            # print("hi")
            # token = jwt.encode(payload, 'hi', algorithm='HS256')

            # response = Response()

            # response.set_cookie(key='jwt', value=token, httponly=True)
            # response.data = {
            #     'jwt': token
            # }
            # print(response,'hi')
            #return redirect('employee:history',response)

        # except:
        #     raise AuthenticationFailed('User not found!')

# class UserView(APIView):

#     def get(self, request):
#         token = request.COOKIES.get('jwt')
#         print(token)

#         if not token:
#             raise AuthenticationFailed('Unauthenticated!')

#         try:
#             payload = jwt.decode(token, 'secret', algorithms=['HS256'])
#             print(payload)
#         except jwt.ExpiredSignatureError:
#             raise AuthenticationFailed('Unauthenticated!')

#         user = Profile.objects.filter(id=payload['id']).first()
#         serializer = ProfileSerializer(user)
#         return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response


class ForgotPass(APIView):
    
    def patch(self,request):
        
        try: 
        
            ps_number = request.data['ps_number']
            pas= request.data['password']
            
            profile = Profile.objects.get(ps_number=ps_number)
            # print("profile:",profile)
            #da = JSONParser().parse(request)
            
            serializer = ProfileSerializer(profile, data={"ps_number": ps_number,"password": pas},partial=True)
            if serializer.is_valid(): 
                serializer.save() 
                response=Response()
                response.data={
                    'message': 'Saved successfully'
                }
            
                return response
        except Profile.DoesNotExist: 
            print("error")
            response=Response()
            response.data={
                'message': 'The Profile with that ps.no does not exist'
            }
            
            return response

def login(request):
    return render(request,'index.html')

def signup(request):
    return render(request,"signup.html")

def reset(request):
    if 'user_id' not in request.session:
        return render(request,"index.html")
    else:
        request.session.clear()
        print("session has been cleared")
        return render(request,"index.html")


def forgotpass(request):
    return render(request,"forgotpass.html")