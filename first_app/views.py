from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord
from first_app.models import User
# from . import forms
from .forms import ContactForm, MyForm
from .forms import NewUserForm

# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {
        'title': 'Django Level Two',
        'access_records': webpages_list
    }
    return render(request, 'first_app/index.html', context=date_dict)

def others(request):
    return render(request, 'first_app/others.html')

def relative(request):
    return render(request, 'first_app/relative_url_template.html')

def new_user(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return users_list(request)
        else:
            print('Form data is invalid!')
    else:
        form = NewUserForm()
    return render(request, 'first_app/users_new.html', {
        'title': 'New User',
        'form': form
    })

# def users(request):
#     user_list = User.objects.order_by('first_name')
#     myDict = {
#         'title': 'Sign Up',
#         'list': user_list
#     }
#     return render(request, 'first_app/users.html', context=myDict)

def users_list(request):
    # user_list = User.objects.order_by('first_name')
    # myDict = {
    #     'title': 'Users List',
    #     'list': user_list
    # }
    return render(request, 'first_app/users_list.html', {
        'title': 'Users List',
        'list': User.objects.order_by('first_name')
    })

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = ContactForm()
    return render(request, 'first_app/contact.html', { 'form': form })

def my_form(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            print('Validation Success!')
            print('Name: {}'.format(form.cleaned_data['name']))
            print('Email: {}'.format(form.cleaned_data['email']))
            print('Text: {}'.format(form.cleaned_data['text']))
    else:
        form = MyForm()

    return render(request, 'first_app/my_form.html', {
        'title': 'Register Form',
        'form': form,
    })

def my_form_old(request):
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

    # return render(request, 'first_app/my_form.html', context=myDict)
    return render(request, 'first_app/my_form.html', {
        'form': myForm,
        'title': 'My Django Form'
    })