from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from iems_app.models import *
from iems_app.forms import CourseModelForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.datastructures import MultiValueDictKeyError
from iems_app.decorators import *


def home(request):
    if request.user and request.user.is_authenticated:
        try:
            student = Student.objects.get(user=request.user.id)
            return redirect('course')
        except ObjectDoesNotExist as e:
            return redirect('teacher_home')

    else:
        return render(request, 'iems_app/unauthorized.html')


# @user_passes_test
def signupuser(request):
    if request.method == 'GET':
        return render(request, 'iems_app/signup.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], '', request.POST['password1'])
                user.save()
                create = Student.objects.create(
                    name=request.POST['name'],
                    department=request.POST['department'],
                    batch_no=request.POST['batch_no'],
                    student_id=request.POST['student_id'],
                    user=user)
                login(request, user)
                return HttpResponse('user created successfully .')
            except IntegrityError:
                return render(request, 'iems_app/signup.html',
                              {'form': UserCreationForm(), 'error': 'Username already exists'})
        else:
            return render(request, 'iems_app/signup.html',
                          {'form': UserCreationForm(), 'error': 'password did not match !'})


def loginuser(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('course')
        else:
            return render(request, 'iems_app/login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'iems_app/login.html', {'form': AuthenticationForm(), 'error': 'User not found !'})
        else:
            login(request, user)
            return redirect('home')


def logoutuser(request):
    logout(request)
    return redirect('login')


@login_required
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
        for item in course_list:
            code = request.POST[item]
            course = Course.objects.get(code=code)
            registration = CourseRegistration.objects.create(student=student, course=course, semester=semester)
            registration.save()

        return redirect('course')


@login_required
def course_list(request):
    env = Environment.objects.get(key='current_semester_id')
    semester = Semester.objects.get(id=env.value)
    student = Student.objects.get(user=request.user)
    registered_courses = CourseRegistration.objects.filter(student=student, semester=semester)
    return render(request, 'iems_app/course.html', {'courses': registered_courses})


@login_required
def student_home(request):
    student = Student.objects.get(user=request.user)
    env = Environment.objects.get(key='current_semester_id')
    semester = Semester.objects.get(id=env.value)
    courses = CourseRegistration.objects.filter(student=student, semester=semester)
    return render(request, 'iems_app/student.html', {'semester': semester, 'courses': courses})


@login_required
def semester_create(request):
    if request.method == 'GET':
        return render(request, 'iems_app/semester.html')
    else:
        get_user = User.objects.get(username=request.user)
        create = Semester.objects.create(name=request.POST['name'], user=get_user)
        return redirect('course')


def teacher_home(request):
    return render(request, 'iems_app/teacher_home.html')


@login_required
@batch_counselor_authorized
def pending_course_reg_student_list(request):
    teacher = Teacher.objects.get(user=request.user)
    counselor = BatchCounselor.objects.get(teacher=teacher)
    students = Student.objects.filter(batch=counselor.batch)
    return render(request, 'iems_app/pending_course_reg_student_list.html', {'students': students})


@batch_counselor_authorized
def pending_course_list_by_student(request, student_id):
    approve_request_id = request.GET.get('approve', 0)
    if approve_request_id != 0:
        teacher = Teacher.objects.get(user=request.user)
        counselor = BatchCounselor.objects.get(teacher=teacher)
        post_data = CourseRegistration.objects.get(id=approve_request_id)
        post_data.approvedBy = counselor
        post_data.save()

    queued_registrations = CourseRegistration.objects.filter(student_id=student_id)
    return render(request, 'iems_app/pending_course_reg_list_by_student.html',
                  {'queued_registrations': queued_registrations, 'sid': student_id})


def routine_insertion(request):
    if request.method == 'GET':
        return render(request, 'iems_app/routine_insertion.html')
    else:
        teacher_name = request.POST.get('teacher')
        teacher = Teacher.objects.get(name=teacher_name)

        semester_name = request.POST.get('semester')
        semester = Semester.objects.get(name=semester_name)

        course_name = request.POST.get('course')
        course = Course.objects.get(name=course_name)

        batch_name = request.POST.get('batch')
        batch = Batch.objects.get(name=batch_name)

        dayOfWeek_name = request.POST.get('dayOfWeek')

        #daysOfWeek =

        post_data = Routine.objects.create(teacher=teacher, semester=semester, course=course, batch=batch,
                                           daysOfWeek_name=dayOfWeek_name)
        post_data.save()
        get_all_data = Routine.objects.all()

        return render(request, 'iems_app/routin_list.html', {'data': get_all_data})

def routine_list(request):
    get_all_data = Routine.objects.all()

    return render(request, 'iems_app/routin_list.html', {'data': get_all_data})