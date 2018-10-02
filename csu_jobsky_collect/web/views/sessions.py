from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from common.models import Sessions
import os

# Create your views here.
def index(request):
    #主页
    return render(request,"web/index.html")


def sessions(request,pIndex):
    #获取招聘会信息
    lists = Sessions.objects.all()
    #分页封装信息
    p = Paginator(lists,10)
    if pIndex == "":
        pIndex="1"
    list2 = p.page(pIndex)
    plist = p.page_range
    context = {"sessionslist":list2,"plist":plist,"pIndex":int(pIndex)}
    return render(request,"web/sessions/index.html",context)


def sessionsAdd(request):
    #加载添加表单
    return render(request,"web/sessions/add.html")


def sessionsInsert(request):
    '''执行招聘会信息的上传插入'''
    try:
        session = Sessions()
        session.uid = request.POST['uid']
        session.enterprise = request.POST['enterprise']
        session.start_time = request.POST['start_time']
        session.place = request.POST['place']
        session.volunteer = request.POST['volunteer']
        session.summary = request.POST['summary']
        session.qr_imgname = request.POST['qr_imgname']
        session.save()
        context = {"info":"招聘会添加成功！"}
    except Exception as e:
        print(e)
        context = {"info":"添加失败！"}

    return render(request,"./web/volunteers/info.html",context)


def sessionsDelete(request,sid):
    try:
        #找到对应的招聘会对象
        ob = Sessions.objects.get(id=sid)
        ob.delete()
        context = {"info":"删除成功！"}
    except Exception as e:
        print(e)
        context = {"info":"删除失败！"}
    return render(request,"./web/volunteers/info.html",context)


def sessionsEdit(request,sid):
    try:
        ob = Sessions.objects.get(id=sid)
        context={"session":ob}
        return render(request,"web/sessions/edit.html",context)
    except Exception as e:
        print(e)
        context = {"info":"没有找到要修改的信息！"}
        return render(request,"web/volunteers/info.html",context)


def sessionsUpdate(request):
    print(request.POST['id'])
    try:
        session = Sessions.objects.get(id=request.POST['id'])
        session.uid = request.POST['uid']
        session.enterprise = request.POST['enterprise']
        session.start_time = request.POST['start_time']
        session.place = request.POST['place']
        session.volunteer = request.POST['volunteer']
        session.summary = request.POST['summary']
        session.qr_imgname = request.POST['qr_imgname']
        session.save()
        context = {"info":"修改成功！"}
    except Exception as e:
        print(e)
        context = {"info":"修改失败！"}
    return render(request,"web/volunteers/info.html",context)
