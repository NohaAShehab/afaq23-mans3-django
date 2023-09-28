
from django.urls import path
from courses.views import index, show, delete, create
urlpatterns = [

    path('', index, name='courses.home'),
    path('<int:course_id>', show, name='courses.show'),
    path('<int:course_id>/delete', delete, name='courses.delete'),
    path('create' ,create, name='courses.create')

]
