from django.shortcuts import render
import os

aHealthyForest = [{}]
dirtAndRoots1 = [{}]
dirtAndRoots2 = [{}]
forestFloor1 = [{}]
forestFloor2 = [{}]
kneeHigh1 = [{}]
kneeHigh2 = [{}]
eyeHigh1 = [{}]
eyeHigh2 = [{}]
skyHigh1 = [{}]
skyHigh2 = [{}]
supportingBiodiversity = [{}]

def home(request):
    return render(request, 'stewardshipProgram/home.html')

def primary(request):
#    for filename in os.listdir('/stewardshipProgram/images'):
#        aHealthyForest.append('/stewardshipProgram/images/'+filename)
    context = {
        'aHealthyForest' : aHealthyForest
    }
    return render(request, 'stewardshipProgram/primary.html', context)

def preschool(request):
    return render(request, 'stewardshipProgram/preschool.html')

def toddler(request):
    return render(request, 'stewardshipProgram/toddler.html')

def resources(request):
    return render(request, 'stewardshipProgram/resources.html')
