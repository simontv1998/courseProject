from django.shortcuts import render

# Create your views here.
def global_action(request):
    context = {}

    if request.method == 'GET':
        return render(request,'clientapp/base.html',context)

