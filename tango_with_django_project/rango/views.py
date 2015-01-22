from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says: Hello world! <br/> <a href='/rango/about'>About</a>")

def about(request):
	return HttpResponse("Rango says this is the about page. <br/> This tutorial has been put together by Jack Croal, 2062685. <br/>Back to <a href='/rango/'>Index</a>. ")

