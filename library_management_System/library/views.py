from typing import ContextManager

import django
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.http import request
from django.shortcuts import HttpResponse, redirect, render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import csv
import io

from library.forms import UserLoginForm, allInformationForm

from .models import *
from .serializers import BookSerializers

# from django.http import JsonResponse


def login_view(request):
    next = request.GET.get("next")
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect("home")

    context = {
        "form": form,
    }

    return render(request, "login.html", context)


def csvImport(request):

    if request.method == "POST":

        csv_file = request.FILES["files"]

        if not csv_file.name.endswith(".csv"):
            message.error(request, "Not a csv file")

        data_set = csv_file.read().decode("UTF-8")
        io_string = io.StrongIO(data_set)
        next(io_string)
        for column in csv.reader(io_string, delimiter=",", quotecher="|"):
            _, created = allInformation.objects.update_or_create(
                Book_serial_Number=column[0],
                Book_name=column[1],
                Authors_Name=column[2],
                Publication_Name=column[3],
                Book_Type=column[4],
                Book_Price=column[5],
                Book_Quantity=column[6],
            )
    return render(request, "csvImport.html")


@login_required
def home(request):

    bookInfo = allInformation.objects.all().order_by("-id")

    context = {
        "bookInfo": bookInfo,
    }
    return render(request, "index.html", context)


@login_required
def addbooks(request):
    form = allInformationForm()
    if request.method == "POST":
        form = allInformationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "addBook.html", context)


@login_required
def update(request, pk):

    book = allInformation.objects.get(id=pk)
    form = allInformationForm(instance=book)
    if request.method == "POST":

        form = allInformationForm(request.POST, instance=book)
        if form.is_valid():

            form.save()
            return redirect("home")
    context = {"form": form}

    return render(request, "addBook.html", context)


def delete(request, pk):
    book = allInformation.objects.get(id=pk)
    if request.method == "POST":
        book.delete()
        return redirect("home")
    context = {"book": book}
    return render(request, "delete.html", context)


@login_required
def logout_view(request):

    logout(request)
    return redirect("login_view")


@api_view(["GET"])
def apiOverview(request):
    api_urls = {
        "Task": "Their URLS",
        "For Looking all the books": "localhost:8000/bookList",
        "For Looking at the specific book": "localhost:8000/bookDetail/<book-id>",
        "For Adding the New Book": "localhost:8000/bookCreate",
        "For Updating any book": "localhost:8000/bookUpdate/<book-id>",
        "For Deleting any specific book": "localhost:8000/bookDelete/<book-id>",
    }

    return Response(api_urls)


@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def bookList(request):
    tasks = allInformation.objects.all().order_by("-id")
    serializer = BookSerializers(tasks, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def bookDetail(request, pk):
    tasks = allInformation.objects.get(id=pk)
    serializer = BookSerializers(tasks, many=False)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def bookCreate(request):
    serializer = BookSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def bookUpdate(request, pk):
    task = allInformation.objects.get(id=pk)
    serializer = BookSerializers(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["DELETE"])
@permission_classes((IsAuthenticated))
def bookDelete(request, pk):
    task = allInformation.objects.get(id=pk)
    task.delete()

    return Response("Item succsesfully delete!")
