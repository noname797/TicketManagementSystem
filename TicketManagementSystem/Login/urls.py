from django.contrib import admin
from django.urls import path
from Login import views

app_name = "login"
urlpatterns=[
    path('',views.login)
]