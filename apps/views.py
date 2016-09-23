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

    # print(models.UserProfile.objects.filter(user=CurrentUserName))

    # Name = User.objects.filter(username=CurrentUserName)
    # if len(Name) != 1:
    #     return HttpResponse('404')

    return render(request, 'home.html', {'UserName': CurrentUserName})


