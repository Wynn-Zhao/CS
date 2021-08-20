from django.shortcuts import render, HttpResponse
from .models import Student

def index(request):
    context = {
        'name': 'Daniyar'
    }
    return render(request, 'student/index.jinja', context)


def bye(request):
    return HttpResponse('Bye, this is bye of student app')


def add(request):
    context = {}
    if (request.method == 'POST'):
        name = request.POST['name']
        yob = request.POST['yob']
        student = Student(name = name, yob = yob)
        student.save()
    return render(request, 'student/add_student.jinja', context)


def students(request):
    context = {}
    students = Student.objects.all()
    context['students'] = students
    return render(request, 'student/students.jinja', context)


def student(request, id):
    context = {}
    s = Student.objects.get(id = id)
    context['student'] = s
    if (request.method == 'POST'):
        s = Student.objects.get(id = id)
        new_name = request.POST['name']
        new_yob = request.POST['yob']
        s.name = new_name
        s.yob = new_yob
        s.save()
    return render(request, 'student/student.jinja', context)


def student_by_year(request, year):
    context = {}
    students = Student.objects.filter(yob = year)
    context['students'] = students
    return render(request, 'student/students.jinja', context)


# --------
# Demostration of session variable in Django
def my_name(request):
    context = {}
    if (request.method == 'POST'):
        request.session['name'] = request.POST['name']
    return render(request, 'name.jinja', context)

