from django.db import models
from students.models import Student
# Create your models here.

# post is written by only one student
class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    body = models.CharField(null=True,blank=True)
    image = models.ImageField(upload_to='posts/images/', null=True, blank=True)
    author = models.ForeignKey(Student, null=True, blank=True, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.title}"