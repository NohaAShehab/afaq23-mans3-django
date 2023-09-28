from django.contrib import admin

# Register your models here.

from  students.models import Student, Track

admin.site.register(Student)

admin.site.register(Track)