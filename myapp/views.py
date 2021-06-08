from django.shortcuts import render,redirect
from datetime import datetime
from django.urls import reverse_lazy
from django.views.generic import FormView, View

from myapp.models import Register
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, login
from django.contrib.auth import authenticate

from .forms import LoginForm

# Create your views here.
def index(request):
    return render(request,"user_login.html")

def admin_login(request):
    if request.method=="POST":
        email= request.POST['email']
        password= request.POST['password']
        user= authenticate(email=email,password=password)
        if user is not None:
            login(request,user)
            messages.info(request,"Login Success")
            return redirect("/")
        else:
            messages.info(request,"invalid credentials")
            return redirect("/")
    return render(request,"admin_login.html")

def user_login(request):
    if request.method=="POST":
        loginemail= request.POST['loginemail']
        loginpassword= request.POST['loginpassword']
        user= authenticate(loginemail=loginemail,loginpassword=loginpassword)
        if user is not None:
            login(request,user)
            messages.info(request,"Login Success")
            return redirect("/")
        else:
            messages.info(request,"invalid credentials")
            return redirect("/")

    else:
       return render(request,"user_login.html")


def register(request):
    if request.method=="POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        password= request.POST.get('password')
        phone= request.POST.get('phone')
        address= request.POST.get('address')
        # if len('phone')!=10:
        #   messages.info(request,'Check your number')
        # else:
        register=Register(name=name,email=email,password=password,phone=phone,address=address,date=datetime.today())
        register.save()
        messages.info(request,'You are registered sucessfully')
        return redirect('/')
    else:
        return render(request,"register.html")


def logoutUser(request):
    logout(request)

    
def user_dash(request):
    return render(request,"user_dash.html")



"""
User login
"""

class LoginView(FormView):
    template_name = "user_login.html"
    form_class = LoginForm
    success_url = reverse_lazy('myapp:register')

    def form_valid(self, form):
        uname = self.request.POST["username"]
        pword = self.request.POST["password"]
        user = authenticate(username=uname, password=pword)
        print("abc",uname)
        if user is not None:
            login(self.request, user)
        else:
            return render(
                self.request,
                self.template_name,
                {"error": "your username doesnot exist", "form": form},
            )
        return super().form_valid(form)