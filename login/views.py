# Create your views here.
from django.shortcuts import render, redirect
from .models import NewUserForm
from django.contrib.auth import login
from django.contrib import messages


def register_request(response):
    if response.method == "POST":
        form = NewUserForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/product/")
    else:
        form = NewUserForm()

    return render(response, "login/view.html", {"form": form})
