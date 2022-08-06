from django.shortcuts import render
from django.http import HttpResponse
from shondesh.models Contract
# Create your views here.
def deshboard(request):
    return render(request,'home.html')
    
def home(request):
    return render(request,'home.html')

def blog(request):
    return render(request,'blog.html')

def about(request):
    return render(request,'about.html')

def contract(request):
    if request.method=='POST':
        print("this is post")
    return render(request,'contract.html')
