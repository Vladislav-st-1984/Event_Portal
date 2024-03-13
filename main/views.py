from django.shortcuts import render, redirect


def index(request):
    return render(request, 'main/base.html')


def eventfunc(request):
    return render(request, 'main/Events.html')


def enentinfofunc(request):
    return render(request, 'main/Eventsinfo.html')


def profilefunc(request):
    return render(request, 'main/profile.html')
