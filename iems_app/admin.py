from django.contrib import admin
from iems_app.models import Course, Student, Faculty, Semester, CourseRegistration,Environment,Teacher,Authorization

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Semester)
admin.site.register(CourseRegistration)
admin.site.register(Environment)
admin.site.register(Teacher)
admin.site.register(Authorization)
