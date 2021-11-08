from django.contrib import admin
from iems_app.models import CourseModel, StudentModel, StaffModel, AdminModel

admin.site.register(CourseModel)
admin.site.register(StudentModel)
admin.site.register(StaffModel)
admin.site.register( AdminModel)
