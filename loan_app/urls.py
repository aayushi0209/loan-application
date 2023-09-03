from django.urls import path
from . import views

urlpatterns = [
    path('', views.EditUserInfo),
    path('register', views.Register),
    path('login1',views.LoginPage),
    path('login_page',views.LoginPage),
    path('logout_page', views.LogoutPage),
    path('loan_request', views.LoanRequest),
    path('loanhistory', views.LoanHistory),
    path('edit_user_info', views.EditUserInfo),
    path('getBalanceSheet',views.GetBalanceSheet)
]
