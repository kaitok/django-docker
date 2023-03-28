from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    resdict = {"resstr": "test"}
    return render(request, "event/index.html", resdict)
