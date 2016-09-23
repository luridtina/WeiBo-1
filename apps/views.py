from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from apps import models


# Create your views here.

def index(request):
    return render(request, 'index.html')


def userprofile(request):
    # 获取用户传入过来的用户名
    CurrentUserName = request.path.split('/')[2]

    # print(models.UserProfile.objects.filter(user=CurrentUserName))

    # Name = User.objects.filter(username=CurrentUserName)
    # if len(Name) != 1:
    #     return HttpResponse('404')
    UserData = {
        'UserName': 'HelloWorld',
        'Brief': '我是签名我是签名我是签名我是签名我是签名我是签名',
        'HeadImg': '/statics/images/1.jpg',
    }

    return render(request, 'userprofile.html', {'UserData': UserData})
