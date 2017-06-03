#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def home_reverse(request):
    return HttpResponseRedirect(reverse('home',args=()))

# Create your views here.
def home(request):
    list = map(int,range(100))
    return render(request,'home.html',{'list':list})