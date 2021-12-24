from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views

app_name="accounts"
urlpatterns = [
    path('signup', views.create_user, name="signup"),
    path('login', views.login_user, name="login"),
    path('forgotpwd', views.Forgotten_password , name="f_pwd"),
    
]
