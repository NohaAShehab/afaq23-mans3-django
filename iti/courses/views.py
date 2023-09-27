from django.shortcuts import render,redirect, reverse
from courses.models import Course
from django.http import HttpResponse
# Create your views here.


# def home(request):
#     return render(request, 'courses/home.html')



def index(request):
    courses = Course.objects.all()
    return render(request, 'courses/home.html', {'courses': courses})


def show(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, 'courses/show.html', {'course': course})


def delete(request, course_id):
    course = Course.objects.get(id=course_id)
    course.delete()
    # return render(request, 'courses/show.html', {'course': course})
    # return  HttpResponse("Delete")
    bact_to_url = reverse('courses.home')
    return redirect(bact_to_url)

