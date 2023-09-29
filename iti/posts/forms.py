
from django import forms

from posts.models import Post

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields= '__all__'


    def clean_title(self):
        title = self.cleaned_data['title']
        if Post.objects.filter(title=title).exists():
            raise forms.ValidationError("This title already exists")

        return title
