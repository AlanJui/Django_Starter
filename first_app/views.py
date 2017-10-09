from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord
from first_app.models import User
from . import forms

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

def my_form(request):
    myForm = forms.MyForm()
    myDict = {
        'title': 'My First Django Form',
        'form': myForm
    }

    if request.method == 'POST':
        form = forms.MyForm(request.POST)
        if form.is_valid():
            print('Validation Success!')
            print('Name: {}'.format(form.cleaned_data['name']))
            print('Email: {}'.format(form.cleaned_data['email']))
            print('Text: {}'.format(form.cleaned_data['text']))
        # else:


    return render(request, 'first_app/my_form.html', context=myDict)