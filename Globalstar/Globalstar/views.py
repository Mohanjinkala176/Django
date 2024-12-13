from django.http import HttpResponse

from django.shortcuts import render

def peddaraju(request):
    return HttpResponse("Hii Kanna") 

def Thingari_paapa(request):
    return HttpResponse("<h1> love you kanna <h1>")

def sample_1(request):
    return render(request,'home.html')