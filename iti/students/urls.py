from django.urls import path

from students.views import  (helloworld, welcome, sayhi, muliplywithten, home,show,
                             index, details, delete, create)
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
    path('create',create, name='students.create' )

    
]
