from django.shortcuts import render, redirect
# Create your views here.
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import SignUpForm


# Create your views here.
def signup(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'login/view.html', context)
