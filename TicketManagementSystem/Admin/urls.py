from django.urls import path,include
from Admin import views


urlpatterns = [
    path("alltickets",views.alltickets,name="alltickets")

]