from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(
        request,
        'articles/index.html',
        context={'app': 'article'},
        )