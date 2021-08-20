from django.shortcuts import render, HttpResponse
from .models import Account

# Create your views here.

def index(request):
    return HttpResponse('<h1>Welcome to accounts application!</h1>')


def create(request, uname, psw):
    account = Account(username = uname, password = psw, money = 0)
    account.save()
    return HttpResponse('Account: {} was created'.format(account))




def change(request, uname, psw, change):
    account = Account.objects.get(username = username)
    try:
        account.money += change
        account.delete()
        account.save()
        return HttpResponse('Save change')
    else:
        return HttpResponse('Something went wrong')







def all(request):
    context = {}
    context['users'] = list(Account.objects.all())
    return render(request, 'users.jinja', context)


def get_username(request, username):
    account = Account.objects.get(username = username)
    return HttpResponse('Id: {}, Account: {}, password: {}'.format(account.id, account, account.password))


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
