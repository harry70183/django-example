# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 11:38:42 2021

@author: harry.chang
"""

from django.http import HttpResponse
from django.shortcuts import render

def here(request):
    return HttpResponse("媽，我在這 !")
def add(request, a, b):
    s = int(a) +int(b)
    return HttpResponse(str(s))
def math(request, a, b):
    a = int(a)
    b = int(b)
    s = a+b
    d = a-b
    p = a*b
    q = a/b
    return render(request, 'math.html',locals())
def menu(request):
    food1 = {'name':'番茄炒蛋', 'price':60, 'comment':'好吃', 'is_spicy':False}
    food2 = {'name':'蒜泥白肉', 'price':100, 'comment':'人氣推薦', 'is_spicy':True}
    foods = [food1,food2]
    return render(request, 'menu.html',locals())
def welcome(request):
    if 'user_name' in request.GET and request.GET['user_name'] != '':
        return HttpResponse('Welcome!~'+request.GET['user_name'])
    else:
        return render(request, 'welcome.html', locals())