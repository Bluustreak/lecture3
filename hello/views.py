from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "hello/index.html")
def brian(request):
    return HttpResponse("hello brian")
def kevin(request):
    return HttpResponse("hello kevman")
# request is a GET command, "GET /hello/harry"
# the variable is the content you send into the template (.NET view) 
def greet(request, name):
    return render(request, "hello/greet.html", {"name":name.capitalize()})

