from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from common.models import Enterprises
from itertools import chain
import os

# Create your views here.
def index(request):
    #主页
    return render(request,"web/index.html")


def enterprises(request,pIndex):
    #获取企业信息
    lists = Enterprises.objects.all()
    #分页封装信息
    p = Paginator(lists,5)
    if pIndex == "":
        pIndex="1"
    list2 = p.page(pIndex)
    print("list2")
    print(list2)
    plist = p.page_range
    context = {"enterpriseslist":list2,"plist":plist,"pIndex":int(pIndex)}
    return render(request,"web/enterprises/index.html",context)


def enterprisesAdd(request):
    #加载添加表单
    return render(request,"web/enterprises/add.html")


def enterprisesInsert(request):
    '''执行企业信息的上传插入'''
    try:
        enterprise = Enterprises()
        enterprise.contacts = request.POST['contacts']
        enterprise.phone = request.POST['phone']
        enterprise.save()
        context = {"info":"添加成功！"}
    except Exception as e:
        print("插入失败")
        print(e)
        context = {"info":"添加失败！"}

    return render(request,"./web/enterprises/info.html",context)


def enterprisesDelete(request,uid):
    try:
        #找到对应的企业对象
        ob = Enterprises.objects.get(id=uid)
        ob.delete()
        context = {"info":"删除成功！"}
    except Exception as e:
        context = {"info":"删除失败！"}
    return render(request,"./web/enterprises/info.html",context)


def enterprisesEdit(request,uid):
    try:
        ob = Enterprises.objects.get(id=uid)
        context={"enterprise":ob}
        return render(request,"web/enterprises/edit.html",context)
    except Exception as e:
        print(e)
        context = {"info":"没有找到要修改的信息！"}
        return render(request,"web/enterprises/info.html",context)


def enterprisesUpdate(request):
    print(request.POST['id'])
    try:
        enterprise = Enterprises.objects.get(id=request.POST['id'])
        enterprise.contacts = request.POST['contacts']
        enterprise.phone = request.POST['phone']
        enterprise.save()
        context = {"info":"修改成功！"}
    except Exception as e:
        print(e)
        context = {"info":"修改失败！"}
    return render(request,"web/enterprises/info.html",context)
