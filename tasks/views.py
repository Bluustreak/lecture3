from django.shortcuts import render

# Create your views here.
taskslist = ["foo", "bar", "baz"]
def index(request):
    return render(request, "tasks/index.html", {"taskslist":taskslist})