from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from common.models import Sessions,Enterprises,Users
from django.db.models import Q
import time,os
from MyQR import myqr
from django.conf import settings

# 网址、保存的二维码名字、保存地址
def generate_qr(site, saveName, saveDir):
    """生成二维码"""
    myqr.run(
        words=site,
		save_dir=saveDir,
		save_name=saveName,
		)

# Create your views here.
def index(request):
    #主页
    return render(request,"web/index.html")


def sessions(request,pIndex):
    #获取招聘会信息
    mod = Sessions.objects
    mywhere=[] #定义一个用于存放搜索条件列表
    # 获取、判断并封装 volunteer 和 enterprise 搜索
    kw = request.GET.get("keywords",None)
    if kw:
        # 查询用户账号中只要含有关键字的都可以
        lists = mod.filter(Q(enterprise__contains=kw)|Q(volunteer__contains=kw))
        mywhere.append("keywords="+kw)
    else:
        lists = mod.filter()

    # lists = Sessions.objects.all()
    #遍历订单信息，查询对应的详情信息
    for se in lists:
        enlist = Enterprises.objects.filter(session_id=se.id)
        se.detaillist = enlist

    print(lists)
    #分页封装信息
    pIndex = int(pIndex)
    page = Paginator(lists,10) #以10条每页创建分页对象
    maxpages = page.num_pages #最大页数
    #判断页数是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex) #当前页数据
    plist = page.page_range   #页码数列表

    #根据账号获取登录者信息
    user = Users.objects.get(id=request.session['volunteers']['id'])

    context = {"sessionslist":list2,"plist":plist,"pIndex":pIndex,'maxpages':maxpages,'mywhere':mywhere,"state":user.state}
    return render(request,"web/sessions/index.html",context)


def sessionsAdd(request):
    #根据账号获取登录者信息
    user = Users.objects.get(id=request.session['volunteers']['id'])

    context = {"uid":request.session['volunteers']['id'],"volunteer":request.session['volunteers']['name'],"state":user.state}
    #加载添加表单
    return render(request,"web/sessions/add.html",context)


def sessionsInsert(request):
    '''执行招聘会信息的上传插入'''
    try:
        #根据账号获取登录者信息
        user = Users.objects.get(id=request.session['volunteers']['id'])

        # 创建招聘会信息
        session = Sessions()
        session.uid = request.POST['uid']
        session.enterprise = request.POST['enterprise']
        session.start_time = request.POST['start_time']
        session.place = request.POST['place']
        session.volunteer = request.POST['volunteer']
        session.person_number = 0
        if session.qr_imgname:
            session.qr_imgname = request.POST['qr_imgname']
        session.save()
        print(session.id)
        # 创建相关企业信息
        enterprise = Enterprises()
        enterprise.uid = request.POST['uid']
        enterprise.session_id = session.id
        enterprise.save()
        # 生成二维码并保存
        site_name = "http://" + settings.DOMAIN + "/" + str(session.id) #网址
        qr_imgname = str(time.time())+"u"+str(session.uid)+"i"+str(session.id)+".png" #二维码名字
        destination = "./static/qr_pics/"   #存放二维码的地址
        generate_qr(site_name, qr_imgname, destination)
        session.qr_imgname = qr_imgname
        session.save()
        context = {"info":"招聘会添加成功！","state":user.state}
    except Exception as e:
        print(e)
        context = {"info":"添加失败！","state":user.state}

    return render(request,"./web/sessions/info.html",context)


def sessionsDelete(request,sid):
    try:
        #根据账号获取登录者信息
        user = Users.objects.get(id=request.session['volunteers']['id'])

        #找到对应的招聘会对象
        sob = Sessions.objects.get(id=sid)
        sob.delete()
        eob = Enterprises.objects.get(session_id=sid)
        eob.delete()
        context = {"info":"删除成功！","state":user.state}
    except Exception as e:
        print(e)
        context = {"info":"删除失败！","state":user.state}
    return render(request,"./web/sessions/info.html",context)


def sessionsEdit(request,sid):
    try:
        #根据账号获取登录者信息
        user = Users.objects.get(id=request.session['volunteers']['id'])
        ob = Sessions.objects.get(id=sid)
        context={"session":ob,"state":user.state}
        return render(request,"web/sessions/edit.html",context)
    except Exception as e:
        print(e)
        context = {"info":"没有找到要修改的信息！","state":user.state}
        return render(request,"web/sessions/info.html",context)


def sessionsUpdate(request):
    print(request.POST['id'])
    try:
        #根据账号获取登录者信息
        user = Users.objects.get(id=request.session['volunteers']['id'])

        session = Sessions.objects.get(id=request.POST['id'])
        session.enterprise = request.POST['enterprise']
        session.start_time = request.POST['start_time']
        session.place = request.POST['place']
        session.summary = request.POST['summary']
        session.person_number = request.POST['person_number']
        session.article = request.POST['article']
        session.save()
        context = {"info":"修改成功！","state":user.state}
    except Exception as e:
        print(e)
        context = {"info":"修改失败！","state":user.state}
    return render(request,"web/sessions/info.html",context)


def sessionsSummary(request,sid):
    try:
        #根据账号获取登录者信息
        user = Users.objects.get(id=request.session['volunteers']['id'])
        ob = Sessions.objects.get(id=sid)
        context={"session":ob,"state":user.state}
        return render(request,"web/sessions/summary.html",context)
    except Exception as e:
        print(e)
        context = {"info":"没有找到总结内容！","state":user.state}
        return render(request,"web/sessions/info.html",context)
