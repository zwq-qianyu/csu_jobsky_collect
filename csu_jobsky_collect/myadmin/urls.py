from django.conf.urls import url

from myadmin.views import index, users

urlpatterns = [
    # 后台首页
    url(r'^$', index.index, name="myadmin_index"),

    # 后台管理员路由
    url(r'^login$', index.login, name="myadmin_login"),
    url(r'^dologin$', index.dologin, name="myadmin_dologin"),
    url(r'^logout$', index.logout, name="myadmin_logout"),
    url(r'^verify$', index.verify, name="myadmin_verify"), #验证码

    # 管理员信息管理路由
    url(r'^users/(?P<pIndex>[0-9]+)$', users.index, name="myadmin_users_index"),
    url(r'^users/add$', users.add, name="myadmin_users_add"),
    url(r'^users/insert$', users.insert, name="myadmin_users_insert"),
    url(r'^users/del/(?P<uid>[0-9]+)$', users.delete, name="myadmin_users_del"),
    url(r'^users/edit/(?P<uid>[0-9]+)$', users.edit, name="myadmin_users_edit"),
    url(r'^users/update/(?P<uid>[0-9]+)$', users.update, name="myadmin_users_update"),
    url(r'^users/editpasswd/(?P<uid>[0-9]+)$', users.editpasswd, name="myadmin_users_editpasswd"),
    url(r'^users/changepasswd/(?P<uid>[0-9]+)$', users.changepasswd, name="myadmin_users_changepasswd"),

    #  # 企业信息管理路由
    # url(r'^enterprises$', enterprises.index, name="myadmin_enterprises_index"),
    # url(r'^enterprises/add/(?P<tid>[0-9]+)$', enterprises.add, name="myadmin_enterprises_add"),
    # url(r'^enterprises/insert$', enterprises.insert, name="myadmin_enterprises_insert"),
    # url(r'^enterprises/del/(?P<tid>[0-9]+)$', enterprises.delete, name="myadmin_enterprises_del"),
    # url(r'^enterprises/edit/(?P<tid>[0-9]+)$', enterprises.edit, name="myadmin_enterprises_edit"),
    # url(r'^enterprises/update/(?P<tid>[0-9]+)$', enterprises.update, name="myadmin_enterprises_update"),
    #
    # # 学生信息管理路由
    # url(r'^students/(?P<pIndex>[0-9]+)$', students.index, name="myadmin_students_index"),
    # url(r'^students/add$', students.add, name="myadmin_students_add"),
    # url(r'^students/insert$', students.insert, name="myadmin_students_insert"),
    # url(r'^students/del/(?P<gid>[0-9]+)$', students.delete, name="myadmin_students_del"),
    # url(r'^students/edit/(?P<gid>[0-9]+)$', students.edit, name="myadmin_students_edit"),
    # url(r'^students/update/(?P<gid>[0-9]+)$', students.update, name="myadmin_students_update"),

]
