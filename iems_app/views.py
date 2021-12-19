from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db import IntegrityError
from iems_app.models import Course, Student, Semester, CourseRegistration, Environment
from iems_app.forms import CourseModelForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.datastructures import MultiValueDictKeyError
from iems_app.decorators import registration_authorized

def home(request):
    if request.user and request.user.is_authenticated:
        return render(request, 'iems_app/base_template.html')
    return render(request, 'iems_app/index.html')

#@user_passes_test
def signupuser(request):
    if request.method == 'GET':
        return render(request, 'iems_app/signup.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1' ] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],'', request.POST['password1'])
                user.save()
                create = Student.objects.create(
                                                                            name=request.POST['name'],
                                                                            department=request.POST['department'],
                                                                            batch_no=request.POST['batch_no'],
                                                                            student_id=request.POST['student_id'],
                                                                            user=user)
                login(request, user)
                return(HttpResponse('user created successfully .'))
            except IntegrityError:
                return render(request, 'iems_app/signup.html', {'form': UserCreationForm(), 'error': 'Username already exists'})
        else:
            return render(request, 'iems_app/signup.html', {'form': UserCreationForm(), 'error': 'password did not match !'})

def loginuser(request):

    if request.method == 'GET':
        return render(request, 'iems_app/login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'iems_app/login.html', {'form': AuthenticationForm(), 'error': 'User not found !'})
        else:
            login(request, user)
            return redirect('course')



def logoutuser(request):
    logout(request)
    return redirect('login')


@login_required
@registration_authorized
def course_registration(request):
    if request.method == 'GET':
        return render(request, 'iems_app/register.html')
    else:
        student = Student.objects.get(user=request.user)
        env = Environment.objects.get(key='current_semester_id')
        semester = Semester.objects.get(id=env.value)
        course_list = [
                            'course_1',
                            'course_2',
                            'course_3',
                            'course_4',
                            'course_5'
        ]
        for item in course_list :
            code = request.POST[item]
            course = Course.objects.get(code=code)
            registration =  CourseRegistration.objects.create(student=student, course=course, semester=semester)
            registration.save()

        return redirect('course')

@login_required
def course_list(request):
    semester = Semester.objects.get(user=request.user)
    student = Student.objects.get(user=request.user)
    registered_courses = CourseRegistration.objects.filter(student=student, semester=semester)
    return render(request, 'iems_app/course.html', {'courses':  registered_courses})

@login_required()
def student_home(request):
    student = Student.objects.get(user=request.user)
    env = Environment.objects.get(key='current_semester_id')
    semester = Semester.objects.get(id=env.value)
    courses = CourseRegistration.objects.filter(student=student, semester=semester)
    return render(request, 'iems_app/student.html', {'semester': semester, 'courses': courses })

@login_required()
def semester_create(request):
    if request.method == 'GET':
        return  render(request, 'iems_app/semester.html')
    else:
        get_user = User.objects.get(username=request.user)
        create = Semester.objects.create(
                                                                    name=request.POST['name'],
                                                                    user=get_user)
        return redirect('course')
