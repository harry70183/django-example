"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from restaurants.views import menu, welcome, list_restaurants, comment
from ashinne.views import index,api_list,login_request,api_logout,register
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls), #後台介面
    path('accounts/login/', login_request), #登入介面
    path('accounts/logout/', api_logout), #登出介面
    path('index/', index), #首頁
    path('', index), #後台的檢視頁面
    path('api_list/', api_list), #進入API介面
    path('accounts/register/', register) #帳號註冊介面
]
