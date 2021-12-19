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
    path('', views.home, name='home'),
]