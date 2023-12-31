from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import SignUpForm

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

def register_user(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authemticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request,username=username,password=password)
            login(request,user)
            messages.success(request,'You have successfuly registered')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request,'register.html',{'form':form})
    return render(request,'register.html',{'form':form})