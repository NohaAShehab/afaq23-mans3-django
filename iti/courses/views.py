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



def create(request):
    print(request)
    if request.method == 'POST':
        request_data = request.POST
        # print(request_data)
        name = request_data['name']
        image = request_data['image']
        max_grade = request_data['max_grade']
        # print(name, image, max_grade)
        course = Course(name=name, max_grade=max_grade, image=image)
        course.save()

        # return HttpResponse("post request accepted")
        bact_to_url = reverse('courses.home')
        return redirect(bact_to_url)
    return render(request, 'courses/create.html')