from django.urls import path
from app.views import *


urlpatterns = [

    path('', main),
    path('main', main),
    path('sign', sign_in),
    path("login_user", login_user),
    path('register', registration),
    path('plain_jain', register_func),
#   path('htt', my_main),
    path('tth', log_out),
    path('sviston', sviston),
    path('Tony-Montana', montana),
    path('shop-gun', shop),
    path('shop-book', shop_book),
    path('shop-book-no', shop_book),
    path('book', list_book_shop),
    path('cart-list', cart_list),
    path('add-cart', add_to_cart),
    path('delete-to-cart', delete_to_cart),


]