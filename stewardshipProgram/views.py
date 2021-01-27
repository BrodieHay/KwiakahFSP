import os
from django.shortcuts import render
from django.conf import settings

aHealthyForest = []
dirtAndRoots1 = []
dirtAndRoots2 = []
forestFloor1 = []
forestFloor2 = []
kneeHigh1 = []
kneeHigh2 = []
eyeHigh1 = []
eyeHigh2 = []
skyHigh1 = []
skyHigh2 = []
supportingBiodiversity = []

def home(request):
    return render(request, 'stewardshipProgram/home.html')

def primary(request):
    aHealthyForest.clear()
    for filename in os.listdir(settings.BASE_DIR / 'stewardshipProgram/static/stewardshipProgram/images/lostSpiritBook'):
        aHealthyForest.append(filename)
    aHealthyForest.sort()
    context = {
        'aHealthyForest' : aHealthyForest,
    }
    return render(request, 'stewardshipProgram/primary.html', context)


def preschool(request):
    return render(request, 'stewardshipProgram/preschool.html')

def toddler(request):
    return render(request, 'stewardshipProgram/toddler.html')

def kidsCorner(request):
    aHealthyForest.clear()
    for filename in os.listdir(settings.BASE_DIR / 'stewardshipProgram/static/stewardshipProgram/images/lostSpiritBook'):
        aHealthyForest.append(filename)
    aHealthyForest.sort()
    context = {
        'aHealthyForest' : aHealthyForest,
    }
    return render(request, 'stewardshipProgram/kidsCorner.html', context)

def resources(request):
    return render(request, 'stewardshipProgram/resources.html')
