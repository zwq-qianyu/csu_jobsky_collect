from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime

class Users(models.Model):
	name = models.CharField(max_length=32)
	password = models.CharField(max_length=32)
	phone = models.CharField(max_length=16)
	email = models.CharField(max_length=50)
	addtime = models.DateTimeField(default=datetime.now)

	class Meta:
		db_table = "user"


class Sessions(models.Model):
	enterprise = models.CharField(max_length=100)
	start_time = models.DateTimeField()
	place = models.CharField(max_length=100)
	volunteer = models.CharField(max_length=32)
	summary = models.TextField()

	class Meta:
		db_table = "session"


class Enterprises(models.Model):
	contacts = models.CharField(max_length=32)
	phone = models.CharField(max_length=16)

	class Meta:
		db_table = "enterprise"


class Students(models.Model):
	school = models.CharField(max_length=100)
	major = models.CharField(max_length=100)
	stu_name = models.CharField(max_length=32)
	phone = models.CharField(max_length=16)

	class Meta:
		db_table = "student"
