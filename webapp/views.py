from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Authenticate
        user = authenticate(request,username= username, password = password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have been successfuly logged in.")
            return redirect('home')
        else:
            messages.success(request,"There is something wrong , please try again or make sure you are registered.")
            return redirect('home')
    else:
        return render(request,'home.html',{})

def logout_user(request):
    logout(request)
    messages.success(request,"You are logged out, hope to see you soon.")
    return redirect('home')