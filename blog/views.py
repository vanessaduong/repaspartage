from django.shortcuts import render

def index(request):
    return render(request, 'blog/index.html', {})

def association(request):
    return render(request, 'blog/association.html', {})

def convives(request):
    return render(request, 'blog/lesconvives.html', {})

def aide(request):
    return render(request, 'blog/nousaider.html', {})
