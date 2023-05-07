from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout  # add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('home')
