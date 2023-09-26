from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# views --> functions

# function accepts http request and returns http response
def helloworld(request):
    return HttpResponse('Hello world')



def welcome(request):
    return HttpResponse('<h1 style="color:red">  Welcome to Django </h1>')


def sayhi(request, username):
    return HttpResponse(f'<h1 style="color:purple">  Hi {username} </h1>')



def muliplywithten(request , num):
    # num = int(num)
    return HttpResponse(f"Result===>{num*10}")

