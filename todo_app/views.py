from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError 
from django.contrib.auth import login,logout,authenticate

def loginform(request):
    if request.method == 'GET':
        return render(request, 'todo_app/loginform.html',{'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password =request.POST['password'])
        if user is None:
            return render(request, 'todo_app/loginuser.html',{'form':AuthenticationForm(), 'error':'Invalid Credentials'})
        else:
            login(request,user)
            return redirect('currenttask')


def logoutform(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
        
def home(request):
    return render(request, 'todo_app/home.html')

def currenttask(request):
    return render(request,'todo_app/currenttask.html')

def signupform(request):
    if request.method == 'GET':
        return render(request,'todo_app/signupform.html',{'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password =request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('currenttask')
            except IntegrityError:
                return render(request, 'todo_app/signupform.html',{'form':UserCreationForm(),'error':'This username has already been taken, Try with different username.'})
        else:
            return render(request, 'todo_app/signupform.html',{'form':UserCreationForm(),'error': "Password didn't match "})