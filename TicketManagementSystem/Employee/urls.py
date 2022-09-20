from django.urls import path
from Employee import views

app_name = "employee"
urlpatterns=[
    path('ticketReq/',views.ticket_request),
    path('reset',views.reset, name="reset"),
    # path('signup',views.signup),
]