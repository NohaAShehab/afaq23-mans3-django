
from django.contrib.auth.decorators import login_required

from posts.views import (CreatePostView, CreatePostGenericView, PostListGenericView,
                         PostDetailGenericView, UpdatePostGenericView, DeletePostGenericView)
from django.urls import path
urlpatterns = [

    path('create',CreatePostView.as_view(), name='posts.create' ),
    path('create/generic',CreatePostGenericView.as_view(), name='posts.create' ),
    path('', PostListGenericView.as_view(), name='posts.index'),
    path('<int:pk>', PostDetailGenericView.as_view(), name='posts.show'),

    path('<int:pk>/edit',login_required( UpdatePostGenericView.as_view()), name='posts.edit'),
    path('<int:pk>/delete', DeletePostGenericView.as_view(), name='posts.delete'),


]
