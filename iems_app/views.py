from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db import IntegrityError
from iems_app.models import CourseModel
from iems_app.forms import CourseModelForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'iems_app/home.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'iems_app/signup.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1' ] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], request.POST['password1'], request.POST['password2'])
                user.save()
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
            registration_courses = CourseModel.objects.all()
            return redirect('course')

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    else:
        return redirect('login')
@login_required
def course_registration(request):
    if request.method == 'GET':
        return render(request, 'iems_app/register.html')
    else:
        course_model = CourseModel.objects.create(
                                            semester=request.POST['semester'],
                                            course_1=request.POST['course_1'],
                                            courses_2=request.POST['courses_2'],
                                            courses_3=request.POST['courses_3'],
                                            courses_4=request.POST['courses_4'],
                                            courses_5=request.POST['courses_5'],
                                            courses_6=request.POST['courses_6'],
                                            courses_7=request.POST['courses_7'],
                                            courses_8=request.POST['courses_8'],
                                            courses_9=request.POST['courses_9'],
                                            )

        return redirect('course')
@login_required
def course_list(request):
    registration_courses = CourseModel.objects.all()
    return render(request, 'iems_app/course.html', {'form': registration_courses })
