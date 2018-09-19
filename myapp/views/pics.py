from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Pics
from PIL import Image
import os

# Create your views here.
def index(request):
    #主页
    return render(request,"myapp/index.html")


def pics(request,pIndex):
    #获取相册信息
    lists = Pics.objects.all()
    #分页封装信息
    p = Paginator(lists,5)
    if pIndex == "":
        pIndex="1"
    list2 = p.page(pIndex)
    plist = p.page_range
    context = {"picslist":list2,"plist":plist,"pIndex":int(pIndex)}
    return render(request,"myapp/pics/index.html",context)


def picsAdd(request):
    #加载添加表单
    return render(request,"myapp/pics/add.html")


def picsInsert(request):
    '''执行图片的上传'''
    myfile = request.FILES.get("mypic",None)
    if not myfile:
        return HttpResponse("没有上传图片信息！")
    try:
        pic = Pics()
        pic.name = request.POST['mypicname']+"."+myfile.name.split('.').pop().lower()  #图片名称
        pic.save()
        context = {"info":"添加成功！"}
    except Exception as e:
        context = {"info":"添加失败！"}
    #新建一个文件并打开存入图片
    dest = open("./static/pics/"+pic.name,"wb+")
    for chunk in myfile.chunks():   #分块写入
        dest.write(chunk)
    dest.close()

    # 执行图片缩放
    im = Image.open("./static/pics/"+pic.name)
    # 缩放到75*75(缩放后的宽高比例不变):
    im.thumbnail((75, 75))
    # 把缩放后的图像用原格式保存:
    im.save("./static/pics/"+pic.name,None)

    return render(request,"./myapp/pics/info.html",context)


def picsDelete(request,uid):
    try:
        #找到对应的图片对象
        ob = Pics.objects.get(id=uid)
        #执行图片删除
        os.remove("./static/pics/"+ob.name)
        ob.delete()
        context = {"info":"删除成功！"}
    except Exception as e:
        context = {"info":"删除失败！"}
    return render(request,"./myapp/pics/info.html",context)


def picsEdit(request,uid):
    try:
        ob = Pics.objects.get(id=uid)
        context={"pic":ob}
        return render(request,"myapp/pics/edit.html",context)
    except Exception as e:
        print(e)
        context = {"info":"没有找到要修改的信息！"}
        return render(request,"myapp/pics/info.html",context)


def picsUpdate(request):
    print(request.POST['id'])
    try:
        pic = Pics.objects.get(id=request.POST['id'])
        #执行图片删除
        os.remove("./static/pics/"+pic.name)
        #上传图片
        myfile1 = request.FILES.get("mypic",None)
        if not myfile1:
            return HttpResponse("没有上传图片信息！")
        #分情况讨论，如果只换图片不换图片名，分类讨论可以防止出现“122.jpg.jpg”这样的名称
        if "." in request.POST['mypicname']:
            pic.name = 's'+request.POST['mypicname']
        else:
            pic.name = request.POST['mypicname']+"."+myfile1.name.split('.').pop().lower()  #图片名称
        pic.save()

        #新建一个文件并打开存入图片
        dest = open("./static/pics/"+pic.name,"wb+")
        for chunk in myfile1.chunks():   #分块写入
            dest.write(chunk)
        dest.close()

        # 执行图片缩放
        im = Image.open("./static/pics/"+pic.name)
        # 缩放到75*75(缩放后的宽高比例不变):
        im.thumbnail((75, 75))
        # 把缩放后的图像用原格式保存:
        im.save("./static/pics/"+pic.name,None)
        context = {"info":"修改成功！"}

    except Exception as e:
        print(e)
        context = {"info":"修改失败！"}
    return render(request,"myapp/pics/info.html",context)