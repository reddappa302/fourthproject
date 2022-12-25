from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def john(request):
    return HttpResponse('<small><marquee>he is a world famous wrestler</marquee></small>')

def johnnydepp(request):
    return HttpResponse('<h1 color="red">lead character of pirates of the carebian</h1>')