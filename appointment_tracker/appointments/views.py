# from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def appointment(request):
    return HttpResponse("Hello, world. You're at the appointment's home page.")
