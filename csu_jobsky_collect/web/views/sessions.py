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
    p = Paginator(lists,5)
    if pIndex == "":
        pIndex="1"
    list2 = p.page(pIndex)
    plist = p.page_range
    context = {"sessionslist":list2,"plist":plist,"pIndex":int(pIndex)}
    return render(request,"web/volunteers/index.html",context)


def sessionsAdd(request):
    #加载添加表单
    return render(request,"web/volunteers/add.html")


def sessionsInsert(request):
    '''执行学生信息的上传插入'''
    try:
        volunteer = Sessions()
        volunteer.enterprise = request.POST['enterprise']
        volunteer.start_time = request.POST['start_time']
        volunteer.place = request.POST['place']
        volunteer.save()
        context = {"info":"添加成功！"}
    except Exception as e:
        print(e)
        context = {"info":"添加失败！"}

    return render(request,"./web/volunteers/info.html",context)


def sessionsDelete(request,uid):
    try:
        #找到对应的招聘会对象
        ob = Sessions.objects.get(id=uid)
        ob.delete()
        context = {"info":"删除成功！"}
    except Exception as e:
        print(e)
        context = {"info":"删除失败！"}
    return render(request,"./web/volunteers/info.html",context)


def sessionsEdit(request,uid):
    try:
        ob = Sessions.objects.get(id=uid)
        context={"volunteer":ob}
        return render(request,"web/volunteers/edit.html",context)
    except Exception as e:
        print(e)
        context = {"info":"没有找到要修改的信息！"}
        return render(request,"web/volunteers/info.html",context)


def sessionsUpdate(request):
    print(request.POST['id'])
    try:
        volunteer = Sessions.objects.get(id=request.POST['id'])
        volunteer.enterprise = request.POST['enterprise']
        volunteer.start_time = request.POST['start_time']
        volunteer.place = request.POST['place']
        volunteer.save()
        context = {"info":"修改成功！"}
    except Exception as e:
        print(e)
        context = {"info":"修改失败！"}
    return render(request,"web/volunteers/info.html",context)
