from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return render(request, "mainapp/index.html")

def homepage(request):
  return render(request, "mainapp/homepage.html")

def profile(request):
  pass
