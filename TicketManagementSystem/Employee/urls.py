from django.urls import path
from Employee import views

app_name = "employee"
urlpatterns=[
    path('raiseReq/',views.raiseReq,name='raiseReq'),
    path('reset',views.reset, name="reset"),
    path('history',views.user_history,name ='history'),
    # path('signup',views.signup),
]