from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

CSE = 'cse'
EEE = 'eee'
Textile = 'textile'

subjects = [
(CSE, 'CSE'),
(EEE, 'EEE'),
(Textile, 'TEXTILE')
]

class StudentModel(models.Model):
    name = models.CharField(max_length=35)
    department = models.CharField(max_length=8, choices=subjects, default=CSE)
    batch_No = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    student_Id = models.CharField(max_length=11)


    def __str__(self):
        return self.name

class CourseModel(models.Model):

    semester = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(8)])
    course_1 = models.CharField(max_length=60)
    courses_2 = models.CharField(max_length=60)
    courses_3 = models.CharField(max_length=60)
    courses_4 = models.CharField(max_length=60)
    courses_5 = models.CharField(max_length=60, null=True, blank=True)
    courses_6 = models.CharField(max_length=60, null=True, blank=True)
    courses_7 = models.CharField(max_length=60, null=True, blank=True)
    courses_8 = models.CharField(max_length=60, null=True, blank=True)
    courses_9 = models.CharField(max_length=60, null=True, blank=True)
    student_user = models.ForeignKey(StudentModel, on_delete=models.CASCADE)



class StaffModel(models.Model):
    name = models.CharField(max_length=35)
    email = models.EmailField()
    staff_user = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_staff':True})

class AdminModel(models.Model):
    name = models.CharField(max_length=35)
    email = models.EmailField()
    admin_user = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_superuser':True})
