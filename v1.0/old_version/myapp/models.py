from django.db import models
from datetime import datetime

# Create your models here.
class Pics(models.Model):
	name = models.CharField(max_length=200);
	addtime = models.DateTimeField(default=datetime.now)

	class Meta:
		db_table = "pics"

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
