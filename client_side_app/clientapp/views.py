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

        #print(request.FILES['file'].read())
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

def topN_action(request):
    context = {}

    if request.method == 'GET':
        return render(request,'clientapp/topN.html',context)


    
