from django.urls import path

from students.views import  (helloworld, welcome, sayhi, muliplywithten, home,show,
                             index, details, delete, create, createViaForm,
                             createViaModelForm, edit)
urlpatterns = [
    path('hello/', helloworld, name='myhello'),
    path('mywelcome/', welcome, name='welcome'),
    path('hi/<username>', sayhi, name='hi'),
    path('mul/<int:num>', muliplywithten, name='mul'),
    path('home/',home, name='home' ),
    path('<int:id>',show, name='students.show' ),
    path('',index,name='students.index' ),
    path('<int:id>/details',details, name='students.details' ),
    path('<int:id>/delete',delete, name='students.delete' ),
    path('create',create, name='students.create' ),
    path('forms/create', createViaForm, name='students.createForm'),
    path('forms/model/create', createViaModelForm, name='students.createForm'),
    path('<int:id>/edit', edit, name='students.edit')


    
]
