from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError 

def usersignup(request):
    if request.method == 'GET':
        return render(request,'todo_app/usersignup.html',{'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password =request.POST['password1'])
                user.save()
            except IntegrityError:
                return render(request, 'todo_app/usersignup.html',{'form':UserCreationForm(),'error':'This username has already been taken, Try with different username.'})
        else:
            return render(request, 'todo_app/usersignup.html',{'form':UserCreationForm(),'error': "Password didn't match "})