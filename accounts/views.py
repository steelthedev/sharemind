from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout
from random import randint
from django.core.mail import send_mail  



# Create your views here.




def create_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        pwd1 = request.POST["pwd1"]
        pwd2 = request.POST["pwd2"]

        if username and pwd1 and pwd2:
            user_fetch = User.objects.filter(username=username)
            if user_fetch.exists():
                messages.info(request, "Username Already Exists")
                return redirect('accounts:signup')
            else:
                if pwd1 != pwd2:
                    messages.info(request, "Passwords Must match")
                    return redirect('accounts:signup')
                else:
                    User.objects.create(username=username , email=email, password = make_password(pwd2))
                    messages.info(request, "You have Successfully Registered")
                    return redirect('home')
        else:
            None      
    return render(request, 'accounts/signup.html' )


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        pwd = request.POST["pwd2"]
        if username and pwd:
            user_fetch = User.objects.get(username = username)
            if user_fetch:
                check_pwd = check_password(pwd , user_fetch.password)
                if not check_pwd:
                    messages.info(request, "Incorrect Passworrd Boss")
                    return redirect('accounts:login')
                else:
                    user = authenticate(request, username = username , password = pwd)
                    if user is not None:
                        login(request, user)
                        return redirect('home')
                    else:
                        messages.info(request, "An Error Occured, Check details Again")
                        return redirect('accounts:login')
            else:
                messages.info(request, "User Does Not Exist")
                return redirect('accounts:login')
        else:
            messages.info(request, "Username and Password Cannot be Empty ")
            return redirect('accounts:login')
    return render(request, 'accounts/login.html')



def Forgotten_password(request):
    if request.method == "POST":
        username = request.POST["username"]
        if username:
            user_fetch = User.objects.get(username = username)

            if user_fetch:
                email = user_fetch.email
                token_generate = randint(0,20)
                to_email= [email]
                message= "Your reset token token is"
                subject = "Forgot Password"
                send_mail(subject, message , 'akinwumikaliyanu@gmail.com' ,to_email ,  fail_silently=False,)
                messages.success(request, "Email Successfully Sent, check your mailbox for the token")
        else:
            None
    return render(request, 'accounts/forgotpwd.html')