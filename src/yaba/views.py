from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'yaba/index.html')


def about(request):
    return render(request, 'yaba/about.html')


def contact(request):
    return render(request, 'yaba/contact.html')

