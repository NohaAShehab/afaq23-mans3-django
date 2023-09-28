from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# views --> functions

# function accepts http request and returns http response

from students.models import Student
def helloworld(request):
    return HttpResponse('Hello world')



def welcome(request):
    return HttpResponse('<h1 style="color:red">  Welcome to Django </h1>')


def sayhi(request, username):
    return HttpResponse(f'<h1 style="color:purple">  Hi {username} </h1>')



def muliplywithten(request , num):
    # num = int(num)
    return HttpResponse(f"Result===>{num*10}")


students = [
        {"id":1, "name":'Noha', "image":"pic1.jpg", 'grade':10 },
        {"id":2, "name":'Noha', "image":"pic2.png", "grade":20 },
        {"id": 3, "name": 'Salma', "image": "pic3.png","grade":30},
        {"id": 4, "name": 'Norhan', "image": "pic4.png","grade":40}
    ]
def home(request):

    return  render(request, 'home.html' ,
                   context = {"name":"noha", 'students':students})


def show(request, id):
    stds = filter(lambda std: std["id"] == id, students)
    # print(list(stds)[0])
    std = list(stds)[0]
    return  render(request, 'students/show.html', context={"student":std})



def index(request):
    # get all students
    # student = Student.objects.all()
    students = Student.get_all_students()
    return render(request, 'students\crud\index.html', context={"students":students})



def details(request, id):
    student = Student.get_specific_student(id)
    return render(request, 'students\crud\show.html', context={"student":student})
