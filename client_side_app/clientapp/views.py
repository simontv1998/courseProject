from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import requests
import json

LOCAL_IP = 'http://127.0.0.1:5000'

# Create your views here.
def global_action(request):
    context = {}

    if request.method == 'GET':
        return render(request,'clientapp/base.html',context)

def upload_action(request):
    context = {}

    if request.method == 'POST':
        # Forward request to server-side app
        # port 5000

        # Fetch file from request 
        for file in request.FILES.getlist('file'):

            # file = request.FILES['file']
            print(file)
            # Use FSStorage API to save file
            # https://docs.djangoproject.com/en/3.2/ref/files/storage/
            fsStorage = FileSystemStorage()
            stored_name = fsStorage.save(file.name, file)

            filepath = fsStorage.location + "/" + stored_name
            request_url = LOCAL_IP+'/upload-files'

            upload_file = {'file': open(filepath, 'rb')}
            upload_data={'file_name': file.name}
            
            response = requests.post(request_url, files=upload_file, data=upload_data)
        
        return render(request,'clientapp/loaded.html',context)
    
    if request.method == 'GET':
        return render(request,'clientapp/loaded.html',context)

def searchTerm_action(request):
    context = {}

    if request.method == 'GET':
        return render(request,'clientapp/searchTerm.html',context)

    if request.method == 'POST':
        if 'term' not in request.POST:
            return render(request,'clientapp/searchTerm.html',context)

        term = request.POST['term']
        # print("term: "+ term)

        upload_data = {'term': term}
        request_url = LOCAL_IP+'/get-freq'
        response = requests.post(request_url, data=upload_data)

        # parse response
        occurList = response.json()
        # print(response.json())

        if len(occurList) == 0:
            return render(request,'clientapp/searchTermCompleted.html',context)

        searchRes = []

        execTime = 0

        for filePath, freq in occurList:
            # print(filePath + ', ' + str(freq))

            # get the execution time
            if freq == -1:
                execTime = float(filePath)
                continue
            
            splits = filePath[filePath.index('/')+1:].rsplit('/', 1)

            # print(splits)

            if (len(splits) <= 1):
                entries = ['N/A', splits[0], freq]
            else:
                entries = [splits[0], splits[1], freq]
            
            searchRes.append(entries)

        context['term'] = term
        context['searchRes'] = sorted(searchRes,key=lambda x: (-x[2],x[0]))
        context['time'] = "{:.4f}".format(execTime)

        return render(request,'clientapp/searchTermCompleted.html',context)

def topN_action(request):
    context = {}

    if request.method == 'GET':
        return render(request,'clientapp/topN.html',context)

    if request.method == 'POST':
        if 'nVal' not in request.POST:
            return render(request,'clientapp/topN.html',context)

        nVal = request.POST['nVal']

        upload_data = {'nVal': nVal}
        request_url = LOCAL_IP+'/get-top-n'
        response = requests.post(request_url, data=upload_data)

        # parse response
        wordFreqMap = response.json()

        context['wordFreqMap'] = wordFreqMap
        context['N'] = nVal

        return render(request,'clientapp/topNCompleted.html',context)

def loaded_action(request):
    context = {}

    if request.method == 'GET':
        return render(request,'clientapp/loaded.html',context)