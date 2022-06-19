# from django.contrib import admin
# from django.urls import path,include
# from . import views

# urlpatterns = [
#     path('', views.register,name='register'),
#     path('login/',views.signin,name='login'),
#     path('home/',views.index,name='index'),
#     path('logout/',views.logoutuser,name='logout'),
    
# ]
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.register,name='register'),
    path('login/',views.signin,name='login'),
    path('home/',views.index,name='index'),
    path('logout/',views.logoutuser,name='logout'),
    path('profile/<id>',views.updateprofile,name='profile'),
    path('newhood/',views.createNeighbourhood,name='newhood'),
    path('neighbourhood/<neighbourhood_id>',views.viewneighbourhood,name='hood'),
    path('join/<neighbourhood_id>',views.join_neighbourhood,name='join'),
    path('leave/<neighbourhood_id>',views.leave_neighbourhood,name='leave')

]