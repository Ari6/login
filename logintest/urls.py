from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('loggedin/', views.LoggedInView.as_view(), name='loggedin')
]
