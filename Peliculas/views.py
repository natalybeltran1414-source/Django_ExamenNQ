from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import PeliculasForm
from .models import Pelicula
     

# Create your views here.
def home(request):
    return render(request, "home.html")

def registry(request):
    if request.method == "POST":
        form = PeliculasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PeliculasForm()
    return render(request, "registry.html", {"form": form})



def signin(request):
    if request.method == "GET":
        return render(request,
                      "signin.html",
                      {"form":AuthenticationForm()})
    else:
        user = authenticate(request,
                            username=request.POST["username"],
                            password =request.POST["password"])
        if user is None:
            return render(request,
                          "signin.html",
                          {"form":AuthenticationForm(),
                           "error":"Usuario o contraseña incorrecta"})
        else:
            login(request, user)
            return redirect("registry")

def signup(request):
    if request.method == "GET":
        return render(request, 
                  "signup.html",
                  {"form":UserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect("registry")

            except IntegrityError:
                return render(request,
                              'signup.html',
                              {"form": UserCreationForm(),
                               "error":"Error al crear el usuario"})
                
        else:
                 return render(request,
                              'signup.html',
                              {"form": UserCreationForm(),
                               "error":"Error, Las contraseñas no coinciden"})

def signout(request):
        logout(request)
        return redirect("home")