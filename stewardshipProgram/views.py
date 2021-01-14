from django.shortcuts import render

def home(request):
    return render(request, 'stewardshipProgram/home.html')

def primary(request):
    return render(request, 'stewardshipProgram/primary.html')

def preschool(request):
    return render(request, 'stewardshipProgram/preschool.html')

def toddler(request):
    return render(request, 'stewardshipProgram/toddler.html')

def resources(request):
    return render(request, 'stewardshipProgram/resources.html')
