from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime

class Enterprises(models.Model):
	enterprise = models.CharField(max_length=200)
	time = models.DateTimeField()
	place = models.CharField(max_length=200)

	class Meta:
		db_table = "enterprise"

class Students(models.Model):
	stu_name = models.CharField(max_length=60)
	school = models.CharField(max_length=200)
	major = models.CharField(max_length=200)
	enterprise = models.CharField(max_length=200)
	time = models.DateTimeField()
	place = models.CharField(max_length=200)

	class Meta:
		db_table = "student"
