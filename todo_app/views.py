from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def usersignup(request):
    return render(request,'todo_app/usersignup.html',{'form':UserCreationForm})