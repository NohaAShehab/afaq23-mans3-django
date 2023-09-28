from django.db import models
from django.shortcuts import  reverse
# Create your models here.

class Track(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.name}'

    @classmethod
    def get_all_tracks(cls):
        return cls.objects.all()

    @classmethod
    def get_specific_track(cls, id):
        return cls.objects.get(id=id)



class Student(models.Model):
    name= models.CharField(max_length=100)
    age = models.IntegerField(default=10,null=True)
    email = models.EmailField(max_length=100, null=True, unique=True)
    image = models.ImageField(upload_to='students/images/', null=True, blank=True)
    track = models.ForeignKey(Track, null=True, blank=True, on_delete=models.CASCADE, related_name='students')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @classmethod
    def get_all_students(cls):
        return  cls.objects.all()

    @classmethod
    def get_specific_student(cls, id):
        return  cls.objects.get(id=id)

    def get_image_url(self):
        return f'/media/{self.image}'

    def get_show_url(self):
        return reverse('students.details',args=[self.id])

    def get_delete_url(self):
        return reverse('students.delete',args=[self.id])