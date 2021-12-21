from django.urls import path
from iems_app import views

urlpatterns=[
    path('login/', views.loginuser, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('signup/', views.signupuser, name='signup'),

    path('course/', views.course_list, name='course'),
    path('semester/', views.semester_create, name='semester'),
    path('register/', views.course_registration, name='register'),
    path('student/', views.student_home, name='student'),
    path('teacher/dashboard', views.teacher_home, name='teacher_home'),
    path('queued_students/', views.pending_course_reg_student_list, name='queued_students'),
    path('queued_approval/<int:student_id>', views.pending_course_list_by_student, name='queued_approval'),
    path('routine_insertion/', views.routine_insertion, name='routine_insertion'),
    path('routine_list/', views.routine_list, name='routine_list'),
    path('', views.home, name='home'),
]