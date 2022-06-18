from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.register,name='register'),
    path('login/',views.signin,name='login'),
    path('home/',views.index,name='index'),
    path('logout/',views.logoutuser,name='logout'),
]
