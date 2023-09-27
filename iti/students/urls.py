from django.urls import path

from students.views import  helloworld, welcome, sayhi, muliplywithten, home,show
urlpatterns = [
    path('hello/', helloworld, name='myhello'),
    path('mywelcome/', welcome, name='welcome'),
    path('hi/<username>', sayhi, name='hi'),
    path('mul/<int:num>', muliplywithten, name='mul'),
    path('home/',home, name='home' ),
    path('<int:id>',show, name='students.show' )
    
]
