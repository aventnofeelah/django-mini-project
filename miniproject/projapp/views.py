from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm, ProductForm
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.http import HttpResponseForbidden

# Create your views here.

def mainRender(request): 
    return render(request, 'main.html')

def profileRender(request, user_id):
    user = get_object_or_404(User, id=user_id)
    products = request.user.products.all()
    return render(request, 'profile.html', {'products' : products,
                                            'user' : user})
def add_productRender(request, user_id):
    if request.user.id != user_id:
        return HttpResponseForbidden("Bad access")
    else:
        if request.method == "POST":
            form = ProductForm(request.POST)
            if form.is_valid():
                product = form.save(commit=False)  
                product.user = request.user  
                product.save()
                return redirect('main_path')
        else:
            form = ProductForm()
    return render(request, 'add-product.html', {'form' : form})
def registrationRender(request):
    if request.method == "POST":
        registform = RegisterForm(request.POST)
        if registform.is_valid():
            user = registform.save(commit=False)
            user.set_password(registform.cleaned_data["password"])
            user.save()
            login(request, user) 
            return redirect('main_path')
    else:
        registform = RegisterForm()
    return render(request, 'register.html', {'form': registform})

def loginRender(request):
    if request.method == "POST":
        loginform = AuthenticationForm(request, data=request.POST)
        if loginform.is_valid():
            user = loginform.get_user()
            login(request, user)
            return redirect('main_path')
    else:
        loginform = AuthenticationForm()
    return render(request, 'login.html', {'form': loginform})

def logoutView(request):
    logout(request)
    return redirect('main_path')
