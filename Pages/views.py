from django.http import HttpResponse
from django.shortcuts import render
from .models import Store, ProjectInfos
from .forms import StoreForm

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home_view.html", {})


def second_view(request, *args, **kwargs):
    my_context = {
        "my_text" : "about me",
        "my_number": 123,
        "mylist": [2,3,4,42,23,23,23,23,23,32,12435234,8]
    }
    return render(request, "second_view.html", my_context)


def project_view(request, *args, **kwargs):
    content = ProjectInfos.objects.all()
    print(content)
    ctx = {
        "objList": content
    }
    return render(request, "project_view.html", ctx)


def createstore_view(request, *args, **kwargs):
    form = StoreForm()
    if request.method == "POST":
        form = StoreForm(request.POST)
        if form.is_valid():
            form.save()
            form = StoreForm()
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    print(Store.objects.count())
    return render(request, "createStore.html", ctx)
