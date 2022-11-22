from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def morning (request):
    return HttpResponse('good morning ,welcome to morning class')
