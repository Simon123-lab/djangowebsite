from django.shortcuts import render


def index(request):
    return render(request,'Layout.html')

def customer(request):
    return render(request,'Customer.html')