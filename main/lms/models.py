from django.db import models
from datetime import datetime
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token



class Log(models.Model):
	application_name = models.CharField(max_length=250)
	log_type = models.CharField(max_length=200)
	added_date = models.DateTimeField(default=datetime.now(), blank=True)
	log_description = models.TextField()


	def __str__(self):    
		""" A string representation of the model Lms"""
		return self.name