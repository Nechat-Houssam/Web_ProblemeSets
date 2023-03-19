from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("Hello, world. You're at the home.")


def add_entry(request):
    return HttpResponse("Hello, world. You're at the add_entry.")