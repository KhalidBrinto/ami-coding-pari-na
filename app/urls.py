from django.urls import path
from  . import views
from rest_framework.authtoken import views as restviews


urlpatterns = [
    path("register/", views.Registration, name="registration"),
    path("login/", views.Login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("", views.Khoj, name="khoj"),
    path("api/getinputvalues", views.get_input_values, name="get_input_values"),
    path('api/gettoken', restviews.obtain_auth_token)
    
]