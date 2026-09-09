from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_twitcher(request):
    """Basic connection check view for the Twitcher application home feed"""
    return HttpResponse("Hello, Twitcher! Welcome to your bird sighting log.")