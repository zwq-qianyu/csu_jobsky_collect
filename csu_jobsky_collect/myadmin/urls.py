from django.conf.urls import url

from myadmin.views import index, users

urlpatterns = [
    # 后台首页
    # url(r'^$', index.index, name="myadmin_index"),

    # 后台管理员路由
    # url(r'^login$', index.login, name="myadmin_login"),
    # url(r'^dologin$', index.dologin, name="myadmin_dologin"),
    # url(r'^logout$', index.logout, name="myadmin_logout"),
    # url(r'^verify$', index.verify, name="myadmin_verify"), #验证码

    # 管理员信息管理路由
    # url(r'^users/(?P<pIndex>[0-9]+)$', users.index, name="myadmin_users_index"),
    # url(r'^users/add$', users.add, name="myadmin_users_add"),
    # url(r'^users/insert$', users.insert, name="myadmin_users_insert"),
    # url(r'^users/del/(?P<uid>[0-9]+)$', users.delete, name="myadmin_users_del"),
    # url(r'^users/edit/(?P<uid>[0-9]+)$', users.edit, name="myadmin_users_edit"),
    # url(r'^users/update/(?P<uid>[0-9]+)$', users.update, name="myadmin_users_update"),
    # url(r'^users/editpasswd/(?P<uid>[0-9]+)$', users.editpasswd, name="myadmin_users_editpasswd"),
    # url(r'^users/changepasswd/(?P<uid>[0-9]+)$', users.changepasswd, name="myadmin_users_changepasswd"),

]
