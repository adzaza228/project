from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import logout
import datetime
from datetime import timedelta
from app.models import block
from app.models import article
from app.models import book
from app.models import cart


def shop(request):
    context = {
        'group': block.objects.all()
    }
    return render(request, 'shopgun.html', context)


def shop_book(request):
    context = {
        'book': book.objects.all()
    }
    return render(request, 'shop_book.html', context)


def list_book_shop(request):
    id_book = request.GET['id']
    context = {
        'book': book.objects.filter(id=id_book)[0]
    }
    return render(request, 'list_book_shop.html', context)



def montana(request):
    return render(request, 'Tony_Montana.html')


def main(request):
    return render(request, 'main.html')


def sviston(request):
    context = {
        'articles': article.objects.all()
    }
    return render(request, 'sviston.html', context)


#def my_main(request):
#    today = datetime.date.today()
 #   start_date = today - timedelta(days=6)
 #   start_date = str(start_date)
#    today = str(today)
#     r = requests.get('https://www.nbrb.by/api/exrates/rates/dynamics/145?startdate=' + start_date + '&enddate=' + today)
#     y = json.loads(r.text)
#     x = 0
#     for i in y:
#         x = x + i['Cur_OfficialRate']
#     x = x/7
#     context = {
#         'Kurs': x
#     }
 #    return render(request, 'main_my.html')


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
        return HttpResponseRedirect('main')


def registration(request):
    return render(request, 'register.html')


def register_func(request):
    try:
        user = User.objects.create_user(
        request.POST['petya'],
        password=request.POST['password'],)

    except Exception as e:
        return HttpResponseRedirect('sign')

    if user is None:
        return HttpResponseRedirect('main')
    else:
        return HttpResponseRedirect('sign')


def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('sign')


def add_to_cart(request):
    try:
        get_cart_user = cart.objects.filter(href_user=request.user)
        if len(get_cart_user) == 0:
            x = cart(href_user=request.user)
            x.save()
        else:
            x = get_cart_user[0]
        x.many_to_many_field.add(
            book.objects.filter(
                id=request.GET['id']
            )[0]
        )
        x.save()
        return HttpResponseRedirect('cart-list')
    except Exception as e:
        return HttpResponseRedirect('sign')


def delete_to_cart(request):
    get_cart_user = cart.objects.filter(href_user=request.user)
    cart_user = get_cart_user[0]
    cart_user.many_to_many_field.remove(book.objects.filter(id=request.GET['id'])[0])
    return HttpResponseRedirect('cart-list')


def cart_list(request):
    context = {'cart': cart.objects.filter(href_user=request.user)[0]}
    return render(request, 'cart.html', context)
