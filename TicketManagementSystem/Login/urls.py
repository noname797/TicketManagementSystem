from django.contrib import admin
from django.urls import path
from Login import views
from Login.views import signup

app_name = "login"
urlpatterns=[
    path('',views.login),
    # path('login',views.login),
    path('signup',views.signup, name='signup'),
    path('reset',views.reset,name="reset")
]