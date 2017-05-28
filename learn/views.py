#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    list = map(str,range(100))
    return render(request,'home.html',{'list':list})