from django.forms import ModelForm
from iems_app.models import Course

class CourseModelForm(ModelForm):
    class Meta():
        model = Course
        fields = '__all__'
