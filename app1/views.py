from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def crr(request):
    return HttpResponse('<h1>impossible</h1>')

def crsr(request):
    return HttpResponse('<h1><marquee>crsr loves vlollyball</marquee></h1>')