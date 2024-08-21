from django.http import HttpResponse
from django.shortcuts import render

def aboutUS(request):
    return HttpResponse("<b>This is about us page</b>")

def homePage(request):
    return render(request,"index.html")