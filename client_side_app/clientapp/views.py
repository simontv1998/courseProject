from django.shortcuts import render

# Create your views here.
def global_action(request):
    context = {}

    if request.method == 'GET':
        return render(request,'clientapp/base.html',context)

def loaded_action(request):
    context = {}

    if request.method == 'GET':
        return render(request,'clientapp/loaded.html',context)

def searchTerm_action(request):
    context = {}

    if request.method == 'GET':
        return render(request,'clientapp/searchTerm.html',context)

def topN_action(request):
    context = {}

    if request.method == 'GET':
        return render(request,'clientapp/topN.html',context)
