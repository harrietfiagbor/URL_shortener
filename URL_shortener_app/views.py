from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.

def home_view(request):
    return HttpResponse("Hello World!")
