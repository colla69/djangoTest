from django.http import HttpResponse
from django.shortcuts import render
from .models import Store
from .forms import RawStoreForm

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
    form = ProjectInfoForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProjectInfoForm(request.POST or None)

    content = ProjectInfos.objects.all()
    print(content)
    ctx = {
        "objList": content
    }
    return render(request, "project_view.html", ctx)


def createstore_view(request, *args, **kwargs):
    form = RawStoreForm()
    if request.method == "POST":
        form = RawStoreForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Store.objects.create()
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    print(Store.objects.count())
    return render(request, "createStore.html", ctx)
