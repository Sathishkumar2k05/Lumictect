from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm

def login_view(request):

    if request.method == "POST":

        form = LoginForm(request, data = request.POST)

        if form.is_valid():

            login(request, form.get_user())

            return redirect("dashboard")

        return render(request, "login.html", {
            "form":form, 
            "error": "Invalid Employee ID or password."
        })

    form = LoginForm()

    return render(request, "login.html", {
        "form": form
    })

def logout_view(request):

    if request.method == "POST":

        logout(request)

        return redirect("login")

    return redirect("dashboard")