from django.shortcuts import render, render_to_response, HttpResponse
from django.contrib.auth.models import User
from apps import models


# Create your views here.

def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def userprofile(request):
    # 获取用户传入过来的用户名
    CurrentUserName = request.path.split('/')[2]
    Code = len(User.objects.filter(username=CurrentUserName))

    if Code != 1:
        return HttpResponse('404')
    UserData = {
        'UserName': 'HelloWorld',
        'Brief': '我是签名我是签名我是签名我是签名我是签名我是签名',
        'HeadImg': '/statics/images/1.jpg',
    }

<<<<<<< HEAD
    return render(request, 'home.html', {'UserName': CurrentUserName})


=======
    return render(request, 'userprofile.html', {'UserData': UserData})
>>>>>>> 1df70817087e84b9e325e31d6951d905d5e9a7dd
