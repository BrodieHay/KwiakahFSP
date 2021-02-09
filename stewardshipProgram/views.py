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
aHealthyForestLiqwala = []
dirtAndRoots1Liqwala = []
dirtAndRoots2Liqwala = []
forestFloor1Liqwala = []
forestFloor2Liqwala = []
kneeHigh1Liqwala = []
kneeHigh2Liqwala = []
eyeHigh1Liqwala = []
eyeHigh2Liqwala = []
skyHigh1Liqwala = []
skyHigh2Liqwala = []
supportingBiodiversityLiqwala = []
booklist = [
    aHealthyForest,
    dirtAndRoots1,
    dirtAndRoots2,
    forestFloor1,
    forestFloor2,
    kneeHigh1,
    kneeHigh2,
    eyeHigh1,
    eyeHigh2,
    skyHigh1,
    skyHigh2,
    supportingBiodiversity,
]

def main():
    for list in booklist:
        list.clear()
    for filename in os.listdir(settings.BASE_DIR / 'stewardshipProgram/static/stewardshipProgram/images/lostSpiritBook'):
        aHealthyForest.append(filename)
    for filename in os.listdir(settings.BASE_DIR / 'stewardshipProgram/static/stewardshipProgram/images/lostSpiritBook'):
        dirtAndRoots2.append(filename)
    for filename in os.listdir(settings.BASE_DIR / 'stewardshipProgram/static/stewardshipProgram/images/lostSpiritBookLiqwala'):
        aHealthyForestLiqwala.append(filename)
    for list in booklist:
        list.sort()

def home(request):
    context = {
        'title':"Home",
    }
    return render(request, 'stewardshipProgram/home.html', context)

def primary(request):
    main()
    context = {
        'title':"Primary",
        'aHealthyForest' : aHealthyForest,
        'dirtAndRoots2' : dirtAndRoots2,
        'forestFloor2' : forestFloor2,
        'kneeHigh2' : kneeHigh2,
        'eyeHigh2' : eyeHigh2,
        'skyHigh2' : skyHigh2,
        'supportingBiodiversity' : supportingBiodiversity,
        'directory' : "lostSpiritBook",
    }
    return render(request, 'stewardshipProgram/primary.html', context)

def preschool(request):
    main()
    context = {
        'title':"Preschool",
        'aHealthyForest' : aHealthyForest,
        'dirtAndRoots1' : dirtAndRoots1,
        'forestFloor1' : forestFloor1,
        'kneeHigh1' : kneeHigh1,
        'eyeHigh1' : eyeHigh1,
        'skyHigh1' : skyHigh1,
        'dirtAndRoots2' : dirtAndRoots2,
        'forestFloor2' : forestFloor2,
        'kneeHigh2' : kneeHigh2,
        'eyeHigh2' : eyeHigh2,
        'skyHigh2' : skyHigh2,
        'supportingBiodiversity' : supportingBiodiversity,

    }
    return render(request, 'stewardshipProgram/preschool.html', context)

def toddler(request):
    main()
    context = {
        'title':"Toddlers",
        'aHealthyForest' : aHealthyForest,
        'dirtAndRoots1' : dirtAndRoots1,
        'forestFloor1' : forestFloor1,
        'kneeHigh1' : kneeHigh1,
        'eyeHigh1' : eyeHigh1,
        'skyHigh1' : skyHigh1,
        'supportingBiodiversity' : supportingBiodiversity,
    }
    return render(request, 'stewardshipProgram/toddler.html', context)

def kidsCorner(request):
    context = {
        'title':"Kid's Corner",

    }
    return render(request, 'stewardshipProgram/kidsCorner.html', context)

def resources(request):
    context = {
        'title':"Resources",
    }
    return render(request, 'stewardshipProgram/resources.html', context)
