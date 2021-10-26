from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.sessions.models import Session
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm
from .models import LoginForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def set_c(request):
    response = HttpResponse('Set your lucky_number as 8')
    response.set_cookie('lucky_number',8)
    return response

def get_c(request):
    if 'lucky_number' in request.COOKIES:
        return HttpResponse('Your lucky_number is {0}'.format(request.COOKIES['lucky_number']))
    else:
        return HttpResponse('No cookies.')

def use_session(request):
    request.session['lucky_number'] = 8
    if 'lucky_number' in request.session:
        lucky_number = request.session['lucky_number']
        #讀取lucky_number
        response = HttpResponse('Your lucky_number is '+ lucky_number)
    del request.session['lucky_number'] #刪除lucky_number
    return response    

def session_test(request):
    sid = request.COOKIES['sessionid']
    s = Session.objects.get(pk=sid)
    s_info = 'Session ID:' + sid + '<br>Expire_date:' + str(s.expire_date) + '<br>Data:' + str(s.get_decoded())
    return HttpResponse(s_info)

def api_logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/index/')    
            
def index(request):
    return render(request, 'index.html', locals())    
    
def api_list(request):
    return render(request, 'api_list.html', locals())    
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/accounts/login/')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', locals())
    
def login_request(request):
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return HttpResponseRedirect("/index/")# Redirect to a success page.
    return render(request, 'login.html', {'login_form': form })    
    
    
    
    
    
    
    
    
    
    
    



    