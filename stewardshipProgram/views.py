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
lostSpiritBook = []
lostSpiritBookLiqwala = []
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
    lostSpiritBook,
    lostSpiritBookLiqwala,

]

def main():
    for list in booklist:
        list.clear()
    for filename in os.listdir(settings.BASE_DIR / 'stewardshipProgram/static/stewardshipProgram/images/aHealthyForest'):
        aHealthyForest.append(filename)
    for filename in os.listdir(settings.BASE_DIR / 'stewardshipProgram/static/stewardshipProgram/images/dirtAndRoots1'):
        dirtAndRoots1.append(filename)
    for filename in os.listdir(settings.BASE_DIR / 'stewardshipProgram/static/stewardshipProgram/images/dirtAndRoots2'):
        dirtAndRoots2.append(filename)
    for filename in os.listdir(settings.BASE_DIR / 'stewardshipProgram/static/stewardshipProgram/images/forestFloor1'):
        forestFloor1.append(filename)
    for filename in os.listdir(settings.BASE_DIR / 'stewardshipProgram/static/stewardshipProgram/images/forestFloor2'):
        forestFloor2.append(filename)
    for filename in os.listdir(settings.BASE_DIR / 'stewardshipProgram/static/stewardshipProgram/images/kneeHigh1'):
        kneeHigh1.append(filename)
    for filename in os.listdir(settings.BASE_DIR / 'stewardshipProgram/static/stewardshipProgram/images/kneeHigh2'):
        kneeHigh2.append(filename)
    for filename in os.listdir(settings.BASE_DIR / 'stewardshipProgram/static/stewardshipProgram/images/eyeHigh1'):
        eyeHigh1.append(filename)
    for filename in os.listdir(settings.BASE_DIR / 'stewardshipProgram/static/stewardshipProgram/images/eyeHigh2'):
        eyeHigh2.append(filename)
    for filename in os.listdir(settings.BASE_DIR / 'stewardshipProgram/static/stewardshipProgram/images/skyHigh1'):
        skyHigh1.append(filename)
    for filename in os.listdir(settings.BASE_DIR / 'stewardshipProgram/static/stewardshipProgram/images/skyHigh2'):
        skyHigh2.append(filename)
    for filename in os.listdir(settings.BASE_DIR / 'stewardshipProgram/static/stewardshipProgram/images/supportingBiodiversity'):
        supportingBiodiversity.append(filename)
    for filename in os.listdir(settings.BASE_DIR / 'stewardshipProgram/static/stewardshipProgram/images/lostSpiritBook'):
        lostSpiritBook.append(filename)
    for filename in os.listdir(settings.BASE_DIR / 'stewardshipProgram/static/stewardshipProgram/images/lostSpiritBookLiqwala'):
        lostSpiritBookLiqwala.append(filename)
    for list in booklist:
        list.sort()



def home(request):
    context = {
        'title':"Home",
    }
    return render(request, 'stewardshipProgram/home.html', context)

def primary(request):
    main()
    directoryName = [
        aHealthyForest,
        dirtAndRoots2,
        forestFloor2,
        kneeHigh2,
        eyeHigh2,
        skyHigh2,
        supportingBiodiversity,
    ]
    directoryList = [
        "aHealthyForest",
        "dirtAndRoots2",
        "forestFloor2",
        "kneeHigh2",
        "eyeHigh2",
        "skyHigh2",
        "supportingBiodiversity",
    ]
    zippedLists = zip(directoryName,directoryList)
    context = {
        'title':"Primary",
        "zippedList" : zippedLists,

    }
    return render(request, 'stewardshipProgram/books.html', context)

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
        'dirtAndRoots' : dirtAndRoots1,
        'forestFloor' : forestFloor1,
        'kneeHigh' : kneeHigh1,
        'eyeHigh' : eyeHigh1,
        'skyHigh' : skyHigh1,
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
