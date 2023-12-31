from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import SignUpForm
from .models import Record

def home(request):
    records = Record.objects.all()
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
        return render(request,'home.html',{'records':records})

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


def customer_record(request,pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request,'record.html',{'customer_record':customer_record})
    else:
        messages.success(request,'You need to login first')
        return redirect('home')
    

def delete_record(request,pk):
    if request.user.is_authenticated:
        delete_item = Record.objects.get(id=pk)
        delete_item.delete()
        messages.success(request,'The record has been deleted sucessfuly')
        return redirect('home')
    else:
        messages.success(request,'You should login first')
        return redirect('home')