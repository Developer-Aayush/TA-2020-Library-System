from django.shortcuts import render, redirect
from .forms import UserLoginForm
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from django.http import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('home')

    context = {
        'form': form,
    }

    return render(request, 'login.html', context)


@login_required
def home(request):

    # code to be written
    return render(request, 'index.html')


def logout_view(request):
    logout(request)
    return redirect('')
