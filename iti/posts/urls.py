


from posts.views import CreatePostView, CreatePostGenericView
from django.urls import path
urlpatterns = [

    path('create',CreatePostView.as_view(), name='posts.create' ),
    path('create/generic',CreatePostGenericViewg.as_view(), name='posts.create' )


]
