from django.conf.urls import url
from . import views
from myapp.views import pics,enterprise,student

urlpatterns = [
	#主页
    url(r'^$', enterprise.index,name="index"),

    #相册信息管理路由
    url(r'^pics/(?P<pIndex>[0-9]+)$', pics.pics, name="pics"),#浏览相册信息、数据分页
    url(r'^pics/add$', pics.picsAdd, name="picsAdd"),#加载添加表单
    url(r'^pics/insert$', pics.picsInsert, name="picsInsert"),#执行相册发布（添加）
    url(r'^pics/delete/(?P<uid>[0-9]+)$', pics.picsDelete, name="picsDelete"),#删除相册信息
    url(r'^pics/edit/(?P<uid>[0-9]+)$', pics.picsEdit, name="picsEdit"),#加载修改信息(编辑）
    url(r'^pics/update$', pics.picsUpdate, name="picsUpdate"),#执行相册修改

    # 企业信息管理路由
    url(r'^enterprise/(?P<pIndex>[0-9]+)$', enterprise.pics, name="enterprise"),		#浏览企业信息、数据分页
    url(r'^enterprise/add$', enterprise.picsAdd, name="enterpriseAdd"),				#加载添加表单
    url(r'^enterprise/insert$', enterprise.picsInsert, name="enterpriseInsert"),		#执行企业发布（添加）
    url(r'^enterprise/delete/(?P<uid>[0-9]+)$', enterprise.picsDelete, name="enterprisesDelete"),	#删除企业信息
    url(r'^enterprise/edit/(?P<uid>[0-9]+)$', enterprise.picsEdit, name="enterpriseEdit"),			#加载修改信息(编辑）
    url(r'^enterprise/update$', enterprise.picsUpdate, name="enterpriseUpdate"),		#执行企业修改
 
    # 学生信息管理路由
    url(r'^student/(?P<pIndex>[0-9]+)$', student.pics, name="student"),		#浏览学生信息、数据分页
    url(r'^student/add$', student.picsAdd, name="studentAdd"),				#加载添加表单
    url(r'^student/insert$', student.picsInsert, name="studentInsert"),		#执行学生发布（添加）
    url(r'^student/delete/(?P<uid>[0-9]+)$', student.picsDelete, name="studentDelete"),	#删除学生信息
    url(r'^student/edit/(?P<uid>[0-9]+)$', student.picsEdit, name="studentEdit"),			#加载修改信息(编辑）
    url(r'^student/update$', student.picsUpdate, name="studentUpdate"),		#执行学生修改
]
