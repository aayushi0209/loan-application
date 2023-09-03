from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate , login , logout
from . forms import UserRegisterForm,UserDataRegisterForm, LoanRequestForm
from django.contrib import messages
from .models import UserData, LoanRequest as LoanRequestModel
from django.contrib.auth.models import User


# Create your views here.
def register(request):
    print(request.method)
    if request.method == 'POST':
        print('req=',request.POST)
        form = UserRegisterForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('/login_page')
        else:
            return render(request, 'register_user.html', {'form': form})
    else:
        form = UserRegisterForm()
        return render(request, 'register_user.html', {'form': form})

def login_page(request):
    return render(request,'login_user.html')

def login1(request):
    if request.method == "POST":
        username = request.POST.get('name1')
        password = request.POST.get('password1')
        nm=username
        user = authenticate(request, username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                nm={'nm':nm}
                return redirect('/home')
            else:
                return redirect('/login_page')
        else:
                return redirect('/login_page')
    else:
        return render(request,'login_user.html')

@login_required(login_url='/register')
def home(request):
    data = User.objects.filter(username=request.user)
    if request.method == 'POST':
        form = UserDataRegisterForm(request.POST)
        form.email = data[0].email
        print( data[0].email, form)
        if form.is_valid():
            form.save()
            return render(request,'home.html', {'message':'Added Sucessfully', 'form': ''});
        else:
            return render(request, 'home.html',{'message':'something went wrong pls try again','form': form })
    new_form = True
    userDataInfo = UserData.objects.all()
    for i in userDataInfo:
        if i.email == request.user:
            new_form =False
            break
    if  new_form:
        form = UserDataRegisterForm()
        return render(request,'home.html',{'form':form});

    else:
        customer = UserData.objects.get(email=request.user)
        form = UserDataRegisterForm(instance=customer)
        return render(request,'home.html',{'form':form, 'message': 'update details'});

@login_required(login_url='/register')
def logout_page(request):
    logout(request)
    return redirect("/")


@login_required(login_url='/register')
def LoanRequest(request):

    form = LoanRequestForm()

    if request.method == 'POST':
        form = LoanRequestForm(request.POST)

        if form.is_valid():
            loan_obj = form.save(commit=False)
            loan_obj.customer = request.user
            form.save()
            return redirect('/')

    return render(request, 'loan_request.html', context={'form': form})

@login_required(login_url='/register')
def LoanHistory(request):
    # return HttpResponse('works')
    loans = LoanRequestModel.objects.filter(
        customer=request.user)
    return render(request, 'loan_history.html', context={'loans': loans})
