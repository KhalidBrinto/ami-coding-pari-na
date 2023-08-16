from django.urls import path
from  . import views
from . import api

urlpatterns = [
    path("register/", views.Registration, name="registration"),
    path("login/", views.Login, name="login"),
    path("", views.Khoj, name="khoj"),
    path("api/getinputvalues", api.get_input_values, name="get_input_values"),
    path("api/gettoken", api.obtain_token),
    
]