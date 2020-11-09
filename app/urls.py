from django.urls import path
from app.views import *


urlpatterns = [
    path('', main),
    path('sign', sign_in),
    path("login_user", login_user),
    path('register', registration),
    path('plain_jain', register_func),
    path('htt', my_main),
    path('tth', log_out),
    path('sviston', sviston),
    path('Tony-Montana', montana),
    path('shop-gun', shop)

]