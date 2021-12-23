from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator


class Batch(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=42)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=30)
    department = models.CharField(max_length=20)
    batch_no = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    student_id = models.CharField(max_length=11)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Semester(models.Model):
    name = models.CharField(max_length=42)
    startDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=16)

    def __str__(self):
        return self.code


class Faculty(models.Model):
    class AllFaculty(models.TextChoices):
        CSE = 'cse', _('CSE')
        EEE = 'eee', _('EEE')
        Textile = 'textile', _('TEXTILE')
        Bba = 'bba', _('BBA')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    facultyName = models.CharField(max_length=64, choices=AllFaculty.choices, default=AllFaculty.CSE)

    def __str__(self):
        return self.user.username


class BatchCounselor(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)

    def __str__(self):
        return self.teacher.name


class CourseRegistration(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    approvedBy = models.ForeignKey(BatchCounselor, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.student.name


class Environment(models.Model):
    key = models.CharField(max_length=128)
    value = models.CharField(max_length=128)

    def __str__(self):
        return self.key


class Routine(models.Model):
    class DayOfWeek(models.TextChoices):
        Saturday = "saturday", _("Saturday")
        Sunday = "sunday", _("Sunday")
        Monday = "monday", _("Monday")
        Tuesday = "tuesday", _("Tuesday")
        Wednesday = "wednesday", _("Wednesday")
        Thursday = "thursday", _("Thursday")
        Friday = "friday", _("Friday")

    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    # startTime = models.DateTimeField()
    # endTime = models.DateTimeField()
    dayOfWeek = models.CharField(max_length=64, choices=DayOfWeek.choices, default="Wednesday")

    def __str__(self):
        return self.teacher.name


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    registeredCourse = models.ForeignKey(CourseRegistration, on_delete=models.CASCADE)
    takenBy = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    dateTime = models.DateTimeField()

    def __str__(self):
        return self.student.name