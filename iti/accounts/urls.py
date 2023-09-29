from django.urls import path, include
from accounts.views import  profile
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/', profile,name='profile' )
]
