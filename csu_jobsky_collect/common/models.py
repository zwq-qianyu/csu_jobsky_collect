from django.db import models
from datetime import datetime


class Users(models.Model):
    """人员信息模型"""
    username = models.CharField(max_length=32)
    name = models.CharField(max_length=16) #真实姓名
    password = models.CharField(max_length=32)
    sex = models.IntegerField(default=1)
    student_id = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=16)
    state = models.IntegerField(default=1)
    addtime = models.DateTimeField(default=datetime.now)

    def toDict(self):
        return {'id':self.id,'sex':self.sex,'name':self.name,'username':self.username,'password':self.password,'student_id':self.student_id,'phone':self.phone,'email':self.email,'state':self.state}

    class Meta:
        db_table = "user"


class Sessions(models.Model):
    uid = models.IntegerField()
    enterprise = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    place = models.CharField(max_length=100)
    volunteer = models.CharField(max_length=32)
    summary = models.TextField(default="总结待填写...")
    qr_imgname = models.CharField(max_length=255)

    class Meta:
        db_table = "session"


class Enterprises(models.Model):
    uid = models.IntegerField()
    session_id = models.IntegerField()
    contacts = models.CharField(max_length=32)
    phone = models.CharField(max_length=16)
    picname = models.CharField(max_length=255)

    class Meta:
        db_table = "enterprise"


class Students(models.Model):
	school = models.CharField(max_length=100)
	major = models.CharField(max_length=100)
	stu_name = models.CharField(max_length=32)
	phone = models.CharField(max_length=16)

	class Meta:
		db_table = "student"
