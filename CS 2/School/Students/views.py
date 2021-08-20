from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student

# TODO: Unable to do functioning href in the jinja file
def index(request):
    return render(request, 'index.jinja')


def delete_all(request):
    Student.objects.all().delete()
    return HttpResponse('<h1>Database deleted</h1>')


def exit(request):
    request.session.clear()
    return redirect(index)


def dashboard(request):
    try: 
        if request.session['login_user']:
            pass
    except:
        return redirect(index)
    context = {}
    context['students'] = Student.objects.all()
    return render(request, 'dashboard.jinja', context)


def register(request):
    try:
        if request.session['login_user']:
            return redirect(dashboard)
    except:
        pass
    context = {}
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        password = request.POST['password']
        origin_country = request.POST['origin_country']
        try:
            if Student.objects.get(firstname = firstname):
                context['message'] = 'this first name already exist, try rename yourself'
                return render(request, 'register.jinja', context)
        except:
            pass
        student = Student(firstname = firstname, lastname = lastname, password = password, origin_country = origin_country)
        student.save()
        return redirect(login)

    return render(request, 'register.jinja', context)


def login(request):
    try:
        if request.session['login_user']:
            return redirect(dashboard)
    except:
        pass
    context = {}
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        password = request.POST['password']
        try:
            s = Student.objects.get(firstname = firstname)
        except:
            context['message'] = 'firstname does not exist in the database'
            return render(request, 'login.jinja', context)

        if s.lastname == lastname:
            if s.password == password:
                request.session['login_user'] = s.firstname
                return redirect(index)
            else:
                context['message'] = 'Wrong password'
        else:
            context['message'] = 'lastname-firstname mismatched'

    return render(request, 'login.jinja', context)


def get_student(request, firstname):
    try: 
        if request.session['login_user']:
            pass
    except:
        return redirect(index)
    try:
        # TODO: here's a problem
        s = Student.objects.get(firstname = firstname)
    except:
        return HttpResponse('Unable to get student from database')
    return HttpResponse("{} {}'s country of origin is {}".format(s.firstname, s.lastname, s.origin_country))


# TODO: This function has bugs
def change(request, firstname):
    try: 
        if request.session['login_user']:
            if request.session['login_user'] == firstname:
                pass
            else:
                return redirect(dashboard)
    except:
        return redirect(index)
    context = {}
    try:
        # TODO: here's a problem
        s = Student.objects.get(firstname = firstname)
    except:
        context['message'] = 'Unable to get Student object from database'
        return render(request, 'change.jinja', context)
    context['self'] = s

    if request.method == 'POST':
        if request.POST['change_firstname']:
            new_firstname = request.POST['firstname']
            try:
                if Student.objects.get(firstname = new_firstname):
                    context['message'] = 'this first name already exist, try rename yourself'
                    return render(request, 'change.jinja', context)
            except:
                s.firstname = new_firstname
                request.session['login_user'] = new_firstname
                s.save()
                context['message'] = 'Rename succeed! Your first name has been changed from {} to {}'.format(firstname, new_firstname)
                return render(request, 'change.jinja', context)

        if request.POST['change_lastname']:
            new_lastname = request.POST['lastname']
            if new_lastname == s.lastname:
                context['message'] = "Don't waste your time"
                return render(request, 'change.jinja', context)
            else:
                s.lastname = new_lastname
                s.save
                context['message'] = 'Rename succeed! Your last name has been changed to {}'.format(new_lastname)
                return render(request, 'change.jinja', context)

        if request.POST['change_password']:
            new_password = request.POST['password']
            if new_password == s.password:
                context['message'] = "Don't waste your time"
                return render(request, 'change.jinja', context)
            else:
                s.password = new_password
                s.save
                context['message'] = 'Changing password succeed! Your password has been changed to {}'.format(new_password)
                return render(request, 'change.jinja', context)

        if request.POST['change_origin_country']:
            new_origin_country = request.POST['origin_country']
            if new_origin_country == s.origin_country:
                context['message'] = "Don't waste your time"
                return render(request, 'change.jinja', context)
            else:
                s.origin_country = new_origin_country
                s.save
                context['message'] = 'Change succeed! Your country of origin has been changed to {}'.format(new_origin_country)
                return render(request, 'change.jinja', context)


    return render(request, 'change.jinja', context)


def delete_account(request):
    try: 
        if request.session['login_user']:
            pass
    except:
        return redirect(index)

    if request.method == 'POST':
        if request.POST['sure']:
            s = Student.objects.get(firstname = request.session['login_user'])
            s.delete()
            return redirect(exit)
        if request.POST['regret']:
            return redirect(index)
    return render(request, 'delete_account.jinja')
