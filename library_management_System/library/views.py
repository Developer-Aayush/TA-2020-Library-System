from typing import ContextManager

import django
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.http import request
from django.shortcuts import HttpResponse, redirect, render

from library.forms import UserLoginForm, allInformationForm


from .models import *
from django.shortcuts import render
# from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializers


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
    return render(request, 'index.html', context)


@login_required
def addbooks(request):
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
        return redirect('home')
    context = {'book': book}
    return render(request, 'delete.html', context)


@login_required
def logout_view(request):

    logout(request)
    return redirect('login_view')


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Task': 'Their URLS',
        'For Looking all the books': 'localhost:8000/bookList',
        'For Looking at the specific book': 'localhost:8000/bookDetail/<book-id>',
        'For Adding the New Book': 'localhost:8000/bookCreate',
        'For Updating any book': 'localhost:8000/bookUpdate/<book-id>',
        'For Deleting any specific book': 'localhost:8000/bookDelete/<book-id>',
    }

    return Response(api_urls)


@api_view(['GET'])
def bookList(request):
    tasks = allInformation.objects.all().order_by('-id')
    serializer = BookSerializers(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def bookDetail(request, pk):
    tasks = allInformation.objects.get(id=pk)
    serializer = BookSerializers(tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def bookCreate(request):
    serializer = BookSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def bookUpdate(request, pk):
    task = allInformation.objects.get(id=pk)
    serializer = BookSerializers(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def bookDelete(request, pk):
    task = allInformation.objects.get(id=pk)
    task.delete()

    return Response('Item succsesfully delete!')
