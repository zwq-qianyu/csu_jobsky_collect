from django.conf.urls import url
from . import views
from web.views import enterprises,students,index,sessions,volunteers

urlpatterns = [
	#主页
    url(r'^$', index.login, name="login"),
    url(r'^(?P<sid>[0-9]+)$', enterprises.index,name="index"),

    # 企业信息管理路由
    url(r'^enterprises/(?P<pIndex>[0-9]+)$', enterprises.enterprises, name="enterprises"),		#浏览企业信息、数据分页
    url(r'^enterprises/add/(?P<sid>[0-9]+)$', enterprises.enterprisesAdd, name="enterprisesAdd"),				#加载添加表单
    url(r'^enterprises/insert/(?P<sid>[0-9]+)$', enterprises.enterprisesInsert, name="enterprisesInsert"),      #执行发布（添加）
    url(r'^enterprises/delete/(?P<sid>[0-9]+)$', enterprises.enterprisesDelete, name="enterprisesDelete"),	#删除企业信息
    url(r'^enterprises/edit/(?P<sid>[0-9]+)$', enterprises.enterprisesEdit, name="enterprisesEdit"),			#加载修改信息(编辑）
    url(r'^enterprises/update$', enterprises.enterprisesUpdate, name="enterprisesUpdate"),		#执行企业修改

    # 学生信息管理路由
    url(r'^students/(?P<pIndex>[0-9]+)$', students.students, name="students"),		#浏览学生信息、数据分页
    url(r'^students/add/(?P<sid>[0-9]+)$', students.studentsAdd, name="studentsAdd"),				#加载添加表单
    url(r'^students/insert/(?P<sid>[0-9]+)$', students.studentsInsert, name="studentsInsert"),      #执行发布（添加）
    url(r'^students/delete/(?P<uid>[0-9]+)$', students.studentsDelete, name="studentsDelete"),	#删除学生信息
    url(r'^students/edit/(?P<uid>[0-9]+)$', students.studentsEdit, name="studentsEdit"),			#加载修改信息(编辑）
    url(r'^students/update$', students.studentsUpdate, name="studentsUpdate"),		#执行学生修改

    # 志愿者登录和退出路由配置
    url(r'^login$', index.login, name="login"),
    url(r'^dologin$', index.dologin, name="dologin"),
    url(r'^logout$', index.logout, name="logout"),

    # 志愿者注册路由
    url(r'^register$', index.register, name="register"),
    url(r'^insert$', index.insert, name="insert"),

    # 志愿者个人中心
    url(r'^volunteers/sessions/(?P<pIndex>[0-9]+)$', volunteers.volun_sessions,name='volunteers_sessions'), #志愿者中心企业信息
    url(r'^volunteers/info$', volunteers.info,name='volunteers_info'), #志愿者中心的个人信息
    url(r'^volunteers/edit$', volunteers.edit,name='volunteers_edit'), #加载修改消息表单
    url(r'^volunteers/update$', volunteers.update,name='volunteers_update'), #执行修改会员信息
    url(r'^volunteers/resetpass$', volunteers.resetpass,name='volunteers_resetpass'), #重置密码表单
    url(r'^volunteers/doresetpass$', volunteers.doresetpass,name='volunteers_doresetpass'), #执行重置密码

    # 志愿者与招聘会信息管理路由
    url(r'^sessions/(?P<pIndex>[0-9]+)$', sessions.sessions, name="sessions"),		#浏览招聘会信息、数据分页
    url(r'^sessions/(?P<sid>[0-9]+)/summary$', sessions.sessionsSummary, name="sessionsSummary"),		#浏览招聘会总结内容
    url(r'^sessions/add$', sessions.sessionsAdd, name="ssessionsAdd"),				#加载添加表单
    url(r'^sessions/insert$', sessions.sessionsInsert, name="sessionsInsert"),      #执行发布（添加）
    url(r'^sessions/delete/(?P<sid>[0-9]+)$', sessions.sessionsDelete, name="sessionsDelete"),	#删除学生信息
    url(r'^sessions/edit/(?P<sid>[0-9]+)$', sessions.sessionsEdit, name="sessionsEdit"),			#加载修改信息(编辑）
    url(r'^sessions/update$', sessions.sessionsUpdate, name="sessionsUpdate"),		#执行修改
]
