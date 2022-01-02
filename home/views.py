from django.shortcuts import render ,HttpResponse
# from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("this is home page")
def about(request):
    return HttpResponse("this is about page")