from django.shortcuts import render
import datetime

# Create your views here.

def index(request):
    datenow = datetime.datetime.now();
    isnewyear = "It's not new year yet"
    if datenow.month is 1 and datenow.day is 1:
        isnewyear = "It's new year!"

    return render(request, "newyear/index.html", {"isnewyear": isnewyear})