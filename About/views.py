from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


def home(request):
    



    return render(request, 'about-us.html')