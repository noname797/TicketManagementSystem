from django.urls import path,include
from Admin import views
from Login.views import reset

app_name = "adminn"
urlpatterns = [
    path("alltickets",views.all_tickets.as_view(),name="alltickets"),
    path("alltickets/<int:id>",views.all_tickets.as_view(),name="alltickets"),
    path("dashboard",views.dashboard.as_view(), name="dashboard"),
    path("reset",reset,name="reset")

]