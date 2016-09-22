from django.shortcuts import render, HttpResponse


# Create your views here.

def index(request):
    return render(request, 'index.html')


def userprofile(request):
    return render(request, 'userprofile.html', {'UserName': 'Hi'})
