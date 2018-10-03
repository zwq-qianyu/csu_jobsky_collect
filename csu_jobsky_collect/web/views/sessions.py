from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from common.models import Sessions,Enterprises
import time,os
from MyQR import myqr

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
    lists = Sessions.objects.all()
    #遍历订单信息，查询对应的详情信息
    for se in lists:
        enlist = Enterprises.objects.filter(session_id=se.id)
        #遍历订单详情，并且获取对应的企业信息（图片）
        # for og in enlist:
        #     og.picname = Goods.objects.only("picname").get(id=og.goodsid).picname
        se.detaillist = enlist

    # context['sessionslist'] = lists
    #分页封装信息
    p = Paginator(lists,10)
    if pIndex == "":
        pIndex="1"
    list2 = p.page(pIndex)
    plist = p.page_range
    context = {"sessionslist":list2,"plist":plist,"pIndex":int(pIndex)}
    return render(request,"web/sessions/index.html",context)


def sessionsAdd(request):
    context = {"uid":request.session['volunteers']['id'],"volunteer":request.session['volunteers']['name']}
    #加载添加表单
    return render(request,"web/sessions/add.html",context)


def sessionsInsert(request):
    '''执行招聘会信息的上传插入'''
    try:
        # 创建招聘会信息
        session = Sessions()
        session.uid = request.POST['uid']
        session.enterprise = request.POST['enterprise']
        session.start_time = request.POST['start_time']
        session.place = request.POST['place']
        session.volunteer = request.POST['volunteer']
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
        site_name = "csu.runtofuture.cn/"+str(session.id) #网址
        qr_imgname = str(time.time())+"u"+str(session.uid)+"i"+str(session.id)+".png" #二维码名字
        destination = "./static/qr_pics/"   #存放二维码的地址
        generate_qr(site_name, qr_imgname, destination)
        session.qr_imgname = qr_imgname
        session.save()
        context = {"info":"招聘会添加成功！"}
    except Exception as e:
        print(e)
        context = {"info":"添加失败！"}

    return render(request,"./web/sessions/info.html",context)


def sessionsDelete(request,sid):
    try:
        #找到对应的招聘会对象
        sob = Sessions.objects.get(id=sid)
        sob.delete()
        eob = Enterprises.objects.get(session_id=sid)
        eob.delete()
        context = {"info":"删除成功！"}
    except Exception as e:
        print(e)
        context = {"info":"删除失败！"}
    return render(request,"./web/sessions/info.html",context)


def sessionsEdit(request,sid):
    try:
        ob = Sessions.objects.get(id=sid)
        context={"session":ob}
        return render(request,"web/sessions/edit.html",context)
    except Exception as e:
        print(e)
        context = {"info":"没有找到要修改的信息！"}
        return render(request,"web/sessions/info.html",context)


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
    return render(request,"web/sessions/info.html",context)
