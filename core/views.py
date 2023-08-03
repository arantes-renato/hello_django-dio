from django.shortcuts import render,HttpResponse

def hello(request):
    return HttpResponse('<h1>Hello Word</h1>')
