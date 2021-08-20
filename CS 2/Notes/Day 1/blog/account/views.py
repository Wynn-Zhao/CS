from django.shortcuts import render, HttpResponse
from .models import Account

def index(request):
    return HttpResponse('<h1>Welcome to accounts application!</h1>')


def create(request, uname, psw):
    account = Account(username = uname, password = psw)
    account.save()
    return HttpResponse('Account: {} was created'.format(account))


def all(request):
    context = {}


    accounts = Account.objects.all()
    context['users'] = list(accounts)
    
    return render(request, 'users.jinja', context)

def get_username(request, username):
    account = Account.objects.get(username = username)
    return HttpResponse('Id: {}, Account: {}, password: {}'.format(account.id,account, account.password))

def get(request, id):
    account = Account.objects.get(id = id)
    return HttpResponse('Id: {}, Account: {}, password: {}'.format(account.id,account, account.password))


def delete(request, uname):
    account = Account.objects.get(username = uname)
    account.delete()
    return HttpResponse('Account was deleted')

def get_password(request, password):
    context = {}
    accounts = Account.objects.filter(password = password)
    context['users'] = list(accounts)
    
    return render(request, 'users.jinja', context)
