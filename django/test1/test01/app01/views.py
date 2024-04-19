from django.shortcuts import render, HttpResponse, redirect  # 重定向：让浏览器自己去请求新内容

from app01.models import UserInfo


# Create your views here.
def index(request):
    # return redirect("http:www.baidu.com") # 重定向到百度页面
    return render(request, "login.html")


def user_list(request):
    return HttpResponse("1111")


def user_add(request):
    return render(request, "user_add.html")  # 会根据顺序依次查找模板文件


#  登录
def login(request):
    if request.method == "GET":
        return render(request, "index.html")
    else:
        print(request.POST)
        if request.POST.get("username") == '' and request.POST.get("password" == ''):
            return HttpResponse("登录成功")
        return render(request, "login.html",
                      {"username": request.POST.get("username")})


def orm(request):
    # 数据表测试

    # 简单分页参考：https://blog.csdn.net/qq_37605109/article/details/124514037

    # 新增
    # UserIdinfo.objects.create(name="xx", password="123", age="18")

    # 删除
    # UserInfo.objects.filter(id=1).delete()  # 删除id=1的数据
    # UserInfo.objects.all().delete() # 删除全部

    # 查询
    # data_lists = UserInfo.objects.all()
    # for obj in data_lists:
    #     print(obj.id)fi

    # data_lists = UserInfo.objects.filter(id=2)  # 获取全部id=2
    # data_lists = UserInfo.objects.filter(id=2).first()  # 获取id=2的第一个
    # print(data_lists.name)

    # 修改
    # UserInfo.objects.all().update(password=111)# 全表密码改为111
    # UserInfo.objects.filter(id=2).update(name="dxx")  # 把id=2的name改成dxx

    return HttpResponse("成功")
