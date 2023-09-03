from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page),
    path('register', views.register),
    path('login1',views.login1),
    path('login_page',views.login_page),
    path('home', views.home),
    path('logout_page', views.logout_page),
    path('loan_request', views.LoanRequest),
    path('loanhistory', views.LoanHistory),
]
