from django.conf.urls import url
from . import views
from web.views import enterprises,students

urlpatterns = [
	#主页
    url(r'^$', enterprises.index,name="index"),

    # 企业信息管理路由
    url(r'^enterprises/(?P<pIndex>[0-9]+)$', enterprises.enterprises, name="enterprises"),		#浏览企业信息、数据分页
    url(r'^enterprises/add$', enterprises.enterprisesAdd, name="enterprisesAdd"),				#加载添加表单
    url(r'^enterprises/insert$', enterprises.enterprisesInsert, name="enterprisesInsert"),      #执行发布（添加）
    url(r'^enterprises/delete/(?P<uid>[0-9]+)$', enterprises.enterprisesDelete, name="enterprisesDelete"),	#删除企业信息
    url(r'^enterprises/edit/(?P<uid>[0-9]+)$', enterprises.enterprisesEdit, name="enterprisesEdit"),			#加载修改信息(编辑）
    url(r'^enterprises/update$', enterprises.enterprisesUpdate, name="enterprisesUpdate"),		#执行企业修改

    # 学生信息管理路由
    url(r'^students/(?P<pIndex>[0-9]+)$', students.students, name="students"),		#浏览学生信息、数据分页
    url(r'^students/add$', students.studentsAdd, name="studentsAdd"),				#加载添加表单
    url(r'^students/insert$', students.studentsInsert, name="studentsInsert"),      #执行发布（添加）
    url(r'^students/delete/(?P<uid>[0-9]+)$', students.studentsDelete, name="studentsDelete"),	#删除学生信息
    url(r'^students/edit/(?P<uid>[0-9]+)$', students.studentsEdit, name="studentsEdit"),			#加载修改信息(编辑）
    url(r'^students/update$', students.studentsUpdate, name="studentsUpdate"),		#执行学生修改
]
