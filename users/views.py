from django.shortcuts import render,redirect
from users.forms import UserRegisterForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.conf import settings
from users.models import User



# User = settings.AUTH_USER_MODEL


def home(request):
    return render(request,'home.html')

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

def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request,f"Hey Youre already logged in")
        return redirect("index")

    if request.method == "POST":
        email = request.POST.get("email")
        password=request.POST.get("password")

        try:
            user=User.objects.get(email=email)
            user = authenticate(request,email=email,password=password)

            if user is not None:
                login(request,user)
                messages.success(request,"You are Logged In")
                return redirect("index")
            else:
                messages.warning(request,"User not Exist,Create an account")

        except:
            messages.warning(request,f"User with {email} does not exist")

        



    return render(request,'login.html')

def logout_view(request):
    logout(request)
    messages.success(request,"You logged out")
    return redirect("login")

def register(request):
    return render(request,'register.html')


