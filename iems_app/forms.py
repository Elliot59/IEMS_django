from django.forms import ModelForm
from iems_app.models import CourseModel

class CourseModelForm(ModelForm):
    class Meta():
        model = CourseModel
        fields = '__all__'
