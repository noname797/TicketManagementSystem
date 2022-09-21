from django.urls import path
from Employee import views
from Employee.views import user_history

app_name = "employee"
urlpatterns=[
    path('raiseReq/',views.raiseReq,name='raiseReq'),
    path('reset',views.reset, name="reset"),
    path('history/',views.user_history.as_view(),name ='history'),
    # path('signup',views.signup),
]