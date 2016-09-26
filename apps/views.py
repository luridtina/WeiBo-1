from django.shortcuts import render, render_to_response, HttpResponse
from django.contrib.auth.models import User
from apps import models

# Create your views here.

# 首页
def index(request):
    
    return render(request, 'index.html')

# 登陆
def login(request):
    return HttpResponse(status=403)

# 个人主页
def userprofile(request):
    # 获取用户传入过来的用户名
    CurrentUserName = request.path.split('/')[2]
    try:
        # 用户信息
        UserInfo = models.UserProfile.objects.get(user__username=CurrentUserName)
        UserData = {
            'name': UserInfo.name,
            'sex': UserInfo.sex,
            'tags': [],
            'head_img': '/' + str(UserInfo.head_img),
            'brief': UserInfo.brief,
            'follow_list': len(UserInfo.follow_list.all()),
            'my_followers': len(UserInfo.my_followers.all())
        }

        for n in UserInfo.tags.all():
            UserData['tags'].append(str(n))

    except Exception as e:
        return HttpResponse('404')

    return render(request, 'userprofile.html', {'UserData': UserData})
