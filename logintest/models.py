from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
	# Add additional field here
	
	def __str__(self):
		return '%s' % (self.email)