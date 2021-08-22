from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home , name="home"),
    path('post_details/<slug:slug>', views.PostDetails , name="post_details"),
    path('feed', views.Feed , name="feed")
]
