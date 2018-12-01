from django.shortcuts import render
from django.views import generic
from .models import CustomUser
from django.contrib.auth import views
# Create your views here.

class LoggedInView(generic.TemplateView):
	model = CustomUser
	template_name = 'loggedin.html'

class LogoutView(views.LogoutView):
	template_name = 'logout.html'

