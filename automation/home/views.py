from django.shortcuts import render
from .forms import *


def Home(request):
    return render(request, 'index.html')
