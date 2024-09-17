from django.shortcuts import render,redirect
from users.forms import UserRegisterForm
from django.contrib.auth import login,authenticate
from django.contrib import messages

def index(request):
    return render(request,'index.html')

def ev_login(request):
    return render(request,'login.html')

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user=form.save()
            username=form.cleaned_data.get("username")
            messages.success(request,f"Hey {username}, You accout was created successfully")
            new_user=authenticate(username=form.cleaned_data['email'],
                                password=form.cleaned_data['password1'])
            login(request,new_user)
            return redirect("index")
    else:
        form = UserRegisterForm()


    context={
        'form':form,
    }
    return render(request,'signup.html',context)

def register(request):
    return render(request,'register.html')


