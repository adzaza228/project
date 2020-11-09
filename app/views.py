from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import logout
import json
import requests
import datetime
from datetime import timedelta
from app.models import block

def shop(request):
    block.objects.all()
    context = {'group': block.objects.all()}
    return render(request, 'shopgun.html', context)

def montana(request):
    return render(request, 'Tony_Montana.html')

def main(request):
    return render(request, 'main.html')

def sviston(request):
    return render(request, 'sviston.html')

def my_main(request):
    today = datetime.date.today()
    start_date = today - timedelta(days=6)
    start_date = str(start_date)
    today = str(today)
    '''r = requests.get('https://www.nbrb.by/api/exrates/rates/dynamics/145?startdate=' + start_date + '&enddate=' + today)
    y = json.loads(r.text)
    x = 0
    for i in y:
        x = x + i['Cur_OfficialRate']
    x = x/7
    context = {
        'Kurs': x
    }'''
    return render(request, 'main_my.html')


def sign_in(request):
    return render(request, 'sign_in.html')


def login_user(request):
    user = authenticate(
        username=request.POST['username'],
        password=request.POST['password']
    )
    if user is None:
        return HttpResponse('Дружище, ты внатуре попутал')
    else:
        login(request, user)
        return HttpResponseRedirect('htt')


def registration(request):
    return render(request, 'register.html')


def register_func(request):
    try:
        user = User.objects.create_user(
        request.POST['petya'],
        password=request.POST['password'],
    )
    except Exception as e:
        return HttpResponseRedirect('sign')

    if user is None:
        return HttpResponseRedirect('htt')
    else:
        return HttpResponseRedirect('sign')

def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponse('')
