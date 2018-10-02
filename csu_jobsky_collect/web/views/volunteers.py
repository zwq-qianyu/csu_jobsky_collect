from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator

from common.models import Users,Sessions

# 公共信息加载函数
def loadinfo(request):
    lists = Types.objects.filter(pid=0)
    context = {'typelist':lists}
    return context

def  volun_sessions(request):
    '''浏览填写的企业信息'''
    context = loadinfo(request)
    #获取当前登录者填写的企业信息
    selist = Sessions.objects.filter(uid=request.session['volunteers']['id'])
    # #遍历订单信息，查询对应的详情信息
    # for od in odlist:
    #     delist = Detail.objects.filter(orderid=od.id)
    #     #遍历订单详情，并且获取对应的商品信息（图片）
    #     for og in delist:
    #         og.picname = Goods.objects.only("picname").get(id=og.goodsid).picname
    #     od.detaillist = delist

    context['aessionslist'] = selist
    return render(request,"web/viporders.html",context)

def odstate(request):
    ''' 修改填写的企业信息 '''
    try:
        sid = request.GET.get("sid",'0')
        ob = Sessions.objects.get(id=oid)
        ob.enterprise = request.GET['enterprise']
        ob.place = request.GET['place']
        ob.start_time = request.GET['start_time']
        ob.save()
        return redirect(reverse('vip_orders'))
    except Exception as err:
        print(err)
        return HttpResponse("信息修改失败！")

def info(request):
    '''加载编辑个人信息页面'''
    try:
        # print(request.session['volunteers']['id'])
        ob = Users.objects.get(id=request.session['volunteers']['id'])
        # print("ob:")
        # print(ob)
        context={"volunteer":ob}
        print("id: "+ str(ob.id))
        return render(request,"web/volunteers/info.html",context)
    except Exception as err:
        print(err)
        context={"info":"没有找到信息！"}
        return render(request,"web/info.html",context)

def edit(request):
    '''加载编辑信息页面'''
    try:
        ob = Users.objects.get(id=request.session['volunteers']['id'])
        context={"vip":ob}
        print("id: "+ str(ob.id))
        return render(request,"web/vip/edit.html",context)
    except Exception as err:
        print(err)
        context={"info":"没有找到要修改的信息！"}
        return render(request,"web/info.html",context)

def update(request):
    '''执行编辑信息'''
    try:
        ob = Users.objects.get(id=request.session['volunteers']['id'])
        ob.name = request.POST['name']
        ob.sex = request.POST['sex']
        ob.address = request.POST['address']
        ob.code = request.POST['code']
        ob.phone = request.POST['phone']
        ob.email = request.POST['email']
        ob.state = 1
        ob.save()
        context={"info":"修改成功！"}
    except Exception as err:
        print(err)
        context={"info":"修改失败"}
    return render(request,"web/info.html",context)

def resetpass(request):
    '''加载重置会员密码信息页面'''
    try:
        ob = Users.objects.get(id=request.session['volunteers']['id'])
        context={"vip":ob}
        return render(request,"web/vip/resetpass.html",context)
    except Exception as err:
        context={"info":"没有找到要修改的信息！"}
        return render(request,"web/info.html",context)

def doresetpass(request):
    '''执行编辑信息'''
    try:
        ob = Users.objects.get(id=request.session['volunteers']['id'])
        #获取密码并md5
        import hashlib
        m = hashlib.md5()
        m.update(bytes(request.POST['password'],encoding="utf8"))
        ob.password = m.hexdigest()
        ob.save()
        #context={"info":"密码重置成功！"}
        return render(request,"web/login.html")
    except Exception as err:
        print(err)
        context={"info":"密码重置失败"}
        return render(request,"web/info.html",context)
