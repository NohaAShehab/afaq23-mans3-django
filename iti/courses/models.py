from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=100)
    max_grade = models.IntegerField(default=0, null=True)
    image = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return self.name
