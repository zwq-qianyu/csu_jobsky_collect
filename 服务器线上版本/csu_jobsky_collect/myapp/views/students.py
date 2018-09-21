from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Students
import os

# Create your views here.
def index(request):
    #主页
    return render(request,"myapp/index.html")


def students(request,pIndex):
    #获取学生信息
    lists = Students.objects.all()
    #分页封装信息
    p = Paginator(lists,5)
    if pIndex == "":
        pIndex="1"
    list2 = p.page(pIndex)
    plist = p.page_range
    context = {"studentslist":list2,"plist":plist,"pIndex":int(pIndex)}
    return render(request,"myapp/students/index.html",context)


def studentsAdd(request):
    #加载添加表单
    return render(request,"myapp/students/add.html")


def studentsInsert(request):
    '''执行学生信息的上传插入'''
    try:
        student = Students()
        student.stu_name = request.POST['name']
        student.school = request.POST['school']
        student.major = request.POST['major']
        student.enterprise = request.POST['enterprise']
        student.time = request.POST['time']
        student.place = request.POST['place']
        student.save()
        context = {"info":"添加成功！"}
    except Exception as e:
        print(e)
        context = {"info":"添加失败！"}

    return render(request,"./myapp/students/info.html",context)


def studentsDelete(request,uid):
    try:
        #找到对应的学生对象
        ob = Students.objects.get(id=uid)
        ob.delete()
        context = {"info":"删除成功！"}
    except Exception as e:
        print(e)
        context = {"info":"删除失败！"}
    return render(request,"./myapp/students/info.html",context)


def studentsEdit(request,uid):
    try:
        ob = Students.objects.get(id=uid)
        context={"student":ob}
        return render(request,"myapp/students/edit.html",context)
    except Exception as e:
        print(e)
        context = {"info":"没有找到要修改的信息！"}
        return render(request,"myapp/students/info.html",context)


def studentsUpdate(request):
    print(request.POST['id'])
    try:
        student = Students.objects.get(id=request.POST['id'])
        student.stu_name = request.POST['name']
        student.school = request.POST['school']
        student.major = request.POST['major']
        student.enterprise = request.POST['enterprise']
        student.time = request.POST['time']
        student.place = request.POST['place']
        student.save()
        context = {"info":"修改成功！"}
    except Exception as e:
        print(e)
        context = {"info":"修改失败！"}
    return render(request,"myapp/students/info.html",context)
