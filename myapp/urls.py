from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('', views.user_login,name='home'),
    # path('index', views.index,name='home'),
    path('admin_login', views.admin_login,name='admin_login'),
    path('user_login', views.user_login,name='user_login'),
    path('register', views.register,name='register'),
    path('logout', views.logoutUser,name='logout'),
    path('user_dash', views.user_dash,name='userdash'),

]