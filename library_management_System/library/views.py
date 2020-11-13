from typing import ContextManager
import django
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.http import request
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse

from library.forms import UserLoginForm, allInformationForm
from .models import *


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

    bookInfo = allInformation.objects.all().order_by('-id')

    context = {'bookInfo': bookInfo,
               }

    # code to be written
    return render(request, 'index.html', context)


@login_required
def addbooks(request):

    # form = addBooks()
    # if request.method == 'POST':
    #     form = addBooks(request.POST)
    #     Book_serial_Number = request.POST["Serial_Number"]
    #     Book_Name = request.POST["Book_Name"]
    #     Book_Type = request.POST["Book_Type"]
    #     Authors_Name = request.POST["Author_Name"]
    #     Book_Price = request.POST["Book_Price"]

    #     bookInfo = allInformation(
    #         Serial_Number=Book_serial_Number,
    #         Book_Name=Book_Name,
    #         Book_Type=Book_Type,
    #         Author_Name=Authors_Name,
    #         Book_Price=Book_Price
    #     )
    #     bookInfo.save()
    #     # message.success(request, 'Book Added Successfully')
    #     redirect('home')

    form = allInformationForm()
    if request.method == 'POST':
        form = allInformationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'addBook.html', context)


@login_required
def update(request, pk):

    book = allInformation.objects.get(id=pk)
    form = allInformationForm(instance=book)
    if request.method == 'POST':

        form = allInformationForm(request.POST, instance=book)
        if form.is_valid():

            form.save()
            return redirect('home')
    context = {'form': form}

    return render(request, 'addBook.html', context)


def delete(request, pk):
    book = allInformation.objects.get(id=pk)
    if request.method == "POST":
        book.delete()
    context = {'book': book}
    return render(request, 'delete.html', context)


def logout_view(request):

    logout(request)
    return redirect('login_view')
