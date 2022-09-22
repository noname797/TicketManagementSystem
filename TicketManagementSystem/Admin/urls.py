from django.urls import path,include
from Admin import views

app_name = "adminn"
urlpatterns = [
    path("alltickets",views.alltickets,name="alltickets"),
    path("dashboard",views.dashboard, name="dashboard"),
    path("reset",views.reset,name="reset")

]