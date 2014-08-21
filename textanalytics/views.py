from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the text analytics index.")
	
def about(request):
    return HttpResponse("Hello, world. You're at the text analytics about page.")