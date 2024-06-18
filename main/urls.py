from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home, name="home"),
    path('sign-up', views.sign_up, name="sign-up"),
    #path('password_change', views.password_change, name="password_change"),
    path('create_post', views.create_post, name="create_post")
]
