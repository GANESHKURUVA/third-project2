from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dhoni(request):
    return HttpResponse("<h1>msd is the coolest captain")

def raina(request):
    return HttpResponse("<h1>he is mr ipl</h1>")
