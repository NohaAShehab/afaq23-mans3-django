

from django import  forms
from students.models import Track, Student



class StudentForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    age = forms.IntegerField(label="Age", required=False)
    email = forms.EmailField(label="Email", max_length=200, required=False)
    image = forms.ImageField(label="Image", required=False)
    track_id = forms.ModelChoiceField(queryset=Track.objects.all(), label="Track", required=False)

    # isvalid , validate --> expected result
    # validate inputs
    def clean_email(self):
        email = self.cleaned_data['email']
        # check if email exists in students --> data not valid
        if Student.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists before")

        return email


#### create form ---> based on Model ?

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def clean_email(self):
        email = self.cleaned_data['email']
        # check if email exists in students --> data not valid
        if Student.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists before")

        return email
