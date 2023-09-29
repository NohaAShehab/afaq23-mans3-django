from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from posts.forms import PostModelForm
from posts.models import Post
from django.views.generic.edit import CreateView

# Create your views here.


# class based views ?

class CreatePostView(View):

    def get(self, request):
        form = PostModelForm()
        return render(request, 'posts/create.html', {'form': form})

    def post(self, request):
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("object added ")

        return render(request, 'posts/create.html', {'form': form})


### generic views


class CreatePostGenericView(CreateView):
    form_class =  PostModelForm
    template_name =  'posts/create.html'
    redirect_url = '/'





