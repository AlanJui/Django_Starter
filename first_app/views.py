from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from first_app.models import Topic,Webpage,AccessRecord
from first_app.models import User
# from . import forms
from .forms import ContactForm, MyForm
from .forms import NewUserForm
from .forms import UserForm, UserProfileInfoForm
from . import models

# Create your views here.

class IndexView(TemplateView):
    template_name = 'first_app/index.html'

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'first_app/school_detail.html'


class CBView(TemplateView):
    template_name = 'first_app/cbv.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inject_me'] = 'BASIC INJECTION!'
        return context

# ====================================================

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {
        'title': 'Django Level Two',
        'access_records': webpages_list
    }
    return render(request, 'first_app/index.html', context=date_dict)

def others(request):
    return render(request, 'first_app/others.html', {
        'title': 'Others Page',
        'text': 'hello world',
        'number': 100,
    })

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

# =======================================================================

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid()        :
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'first_app/registration.html', {
        'registered': registered,
        'user_form': user_form,
        'profile_form': profile_form
    })

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account Not Active!!')
        else:
            print('Someone tried to login and failed!')
            print('Username: {} and password {}'.format(username, password))
            return HttpResponse('Invalid login details supplied!')
    else:
        return render(request, 'first_app/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

