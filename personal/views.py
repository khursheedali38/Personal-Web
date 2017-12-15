"""This script helps us define whatever user can view and what to render when user requests are received"""

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'personal/home.html') 

def tutorials(request):
    return render(request, 'personal/basic.html', {'content':['staty tunedIf you would like to contact me regarding any project related discussions. Please email me.', 'khursheedali38@gmail.com']})
