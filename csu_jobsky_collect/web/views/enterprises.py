from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse
from common.models import Enterprises,Sessions
import os

# Create your views here.
def index(request,sid):
    context = {"session_id":sid}
    #主页
    return render(request,"web/index.html",context)


def enterprises(request,pIndex):
    #获取企业信息
    lists = Enterprises.objects.all()
    #遍历订单信息，查询对应的详情信息
    for en in lists:
        enlist = Sessions.objects.filter(id=en.session_id)
        en.detaillist = enlist
    #分页封装信息
    p = Paginator(lists,10)
    if pIndex == "":
        pIndex="1"
    list2 = p.page(pIndex)
    print("list2")
    print(list2)
    plist = p.page_range
    context = {"enterpriseslist":list2,"plist":plist,"pIndex":int(pIndex)}
    return render(request,"web/enterprises/index.html",context)


def enterprisesAdd(request,sid):
    enterprise = Enterprises.objects.get(session_id=sid)
    session = Sessions.objects.get(id=sid)
    # print(session.id)
    context = {"session": session}
    print(enterprise.contacts)
    if (enterprise.contacts is not None) and (enterprise.contacts != ""):
        print(sid)
        return HttpResponseRedirect(reverse('enterprisesEdit', kwargs={'sid': sid}))
    #加载添加表单
    return render(request,"web/enterprises/add.html",context)


def enterprisesInsert(request,sid):
    '''执行企业信息的上传插入'''
    try:
        enterprise = Enterprises.objects.get(session_id=sid)
        enterprise.contacts = request.POST['contacts']
        enterprise.phone = request.POST['phone']
        enterprise.save()
        context = {"info":"添加成功！"}
    except Exception as e:
        print("插入失败")
        print(e)
        context = {"info":"添加失败！"}

    return render(request,"./web/enterprises/info.html",context)


def enterprisesDelete(request,sid):
    try:
        #找到对应的企业对象
        ob = Enterprises.objects.get(session_id=sid)
        ob.delete()
        context = {"info":"删除成功！"}
    except Exception as e:
        context = {"info":"删除失败！"}
    return render(request,"./web/enterprises/info.html",context)


def enterprisesEdit(request,sid):
    try:
        session = Sessions.objects.get(id=sid)
        enterprise = Enterprises.objects.get(session_id=sid)
        context = {"enterprise":enterprise}
        context['session'] = session
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
