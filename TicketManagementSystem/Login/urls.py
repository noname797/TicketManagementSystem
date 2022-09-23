from django.contrib import admin
from django.urls import path,include
from Login import views
from rest_framework import routers
from .views import ProfileViewSet,RegisterView, LoginView, LogoutView,ForgotPass
app_name = "login"

#router = routers.DefaultRouter()
#router.register(r'profile', ProfileViewSet)

urlpatterns=[
    path('',views.reset,name="reset"),
    path("signup",views.signup,name="signup"),
    #path('reset',views.reset,name="reset"),
    #path("",include(router.urls)),
    path("login",views.login,name="login"),
    path('register-api', RegisterView.as_view(),name='register-api'),
    path('forgotpass-api', ForgotPass.as_view(),name='forgotpass-api'),

    path('login-api', LoginView.as_view(),name='login-api'),
    # path('user', UserView.as_view(),name='user'),
    path('logout', LogoutView.as_view(),name='logout'),
    path("forgotpass",views.forgotpass,name="forgotpass"),
]

