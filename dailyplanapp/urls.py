from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.index),
    path("<int:day>", view=views.daily_diet_by_number),
    path("<str:day>", view=views.daily_diet,name="daily-diet"),
    
    

]
