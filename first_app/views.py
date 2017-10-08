from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord
from first_app.models import User

# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {
        'title': 'Django Level Two',
        'access_records': webpages_list
    }
    return render(request, 'first_app/index.html', context=date_dict)

def users(request):
    user_list = User.objects.order_by('first_name')
    myDict = {
        'title': 'Users List',
        'list': user_list
    }
    return render(request, 'first_app/users.html', context=myDict)