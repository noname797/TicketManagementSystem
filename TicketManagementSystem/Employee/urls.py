from django.urls import path
from Employee import views
from Employee.views import user_history,raiseReq

app_name = "employee"
urlpatterns=[
    path('raiseReq/<int:id>',views.raiseReq.as_view(),name='raiseReq'),
    # path('create_tic/<int:id>',views.create_ticket.as_view(),name='create_ticket'),
    path('reset',views.reset, name="reset"),
    path('history/<int:id>',views.user_history.as_view(),name ='history'),
    # path('signup',views.signup),
]