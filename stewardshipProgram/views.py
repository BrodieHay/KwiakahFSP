import os
from django.shortcuts import render
from django.conf import settings

aHealthyForest = []
forestFloor = []
kneeHigh = []
eyeHigh = []
skyHigh = []
lostSpiritBook = []
lostSpiritBookLiqwala = []
booklist = [
    aHealthyForest,
    forestFloor,
    kneeHigh,
    eyeHigh,
    skyHigh,
    lostSpiritBook,
    lostSpiritBookLiqwala,

]

tabName = [
    "Soil",
    "The Forest Floor",
    "Knee High",
    "Eye High",
    "Sky High",
]
directoryName = [
    aHealthyForest,
    forestFloor,
    kneeHigh,
    eyeHigh,
    skyHigh,
]
directoryList = [
    "aHealthyForest",
    "forestFloor",
    "kneeHigh",
    "eyeHigh",
    "skyHigh",
]


def main():
    for list in booklist:
        list.clear()
    for filename in os.listdir(settings.BASE_DIR / 'stewardshipProgram/static/stewardshipProgram/images/aHealthyForest'):
        aHealthyForest.append(filename)
    for filename in os.listdir(settings.BASE_DIR / 'stewardshipProgram/static/stewardshipProgram/images/forestFloor'):
        forestFloor.append(filename)
    for filename in os.listdir(settings.BASE_DIR / 'stewardshipProgram/static/stewardshipProgram/images/kneeHigh'):
        kneeHigh.append(filename)
    for filename in os.listdir(settings.BASE_DIR / 'stewardshipProgram/static/stewardshipProgram/images/eyeHigh'):
        eyeHigh.append(filename)
    for filename in os.listdir(settings.BASE_DIR / 'stewardshipProgram/static/stewardshipProgram/images/skyHigh'):
        skyHigh.append(filename)
    for list in booklist:
        list.sort()



def home(request):
    context = {
        'title':"Home",
    }
    return render(request, 'stewardshipProgram/home.html', context)

def primary(request):
    main()
    zippedTabs = zip(tabName,directoryList)
    zippedLists = zip(directoryName,directoryList)
    context = {
        'title':"Primary",
        'tabName' : zippedTabs,
        'zippedList' : zippedLists,

    }
    return render(request, 'stewardshipProgram/primary.html', context)

def preschool(request):
    main()
    zippedTabs = zip(tabName,directoryList)
    zippedLists = zip(directoryName,directoryList)
    context = {
        'title':"Preschool",
        'tabName' : zippedTabs,
        'zippedList' : zippedLists,

    }
    return render(request, 'stewardshipProgram/preschool.html', context)

def toddler(request):
    main()
    zippedTabs = zip(tabName,directoryList)
    zippedLists = zip(directoryName,directoryList)
    context = {
        'title':"Toddler",
        'tabName' : zippedTabs,
        'zippedList' : zippedLists,

    }
    return render(request, 'stewardshipProgram/toddler.html', context)

def kidsCorner(request):
    context = {
        'title':"Kid's Corner",

    }
    return render(request, 'stewardshipProgram/kidsCorner.html', context)

def curriculumBackground(request):
    context = {
        'title':"Curriculum Background",
    }
    return render(request, 'stewardshipProgram/curriculumBackground.html', context)

def resources(request):
    context = {
        'title':"Resources",
    }
    return render(request, 'stewardshipProgram/resources.html', context)

def contactUs(request):
    context = {
        'title':"Contact Us",
    }
    return render(request, 'stewardshipProgram/contactUs.html', context)
