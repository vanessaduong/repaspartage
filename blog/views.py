from django.shortcuts import render

def index(request):
    return render(request, 'blog/index.html', {})

def association(request):
    return render(request, 'blog/association.html', {})

def convives(request):
    return render(request, 'blog/lesconvives.html', {})

def aide(request):
    return render(request, 'blog/nousaider.html', {})

def benevoles(request):
    return render(request, 'blog/lesbenevoles.html', {})

def membres(request):
    return render(request, 'blog/dejabenevole.html', {})
