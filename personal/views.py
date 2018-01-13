"""This script helps us define whatever user can view and what to render when user requests are received"""

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'personal/home.html') 

def projects(request):
    return render(request, 'personal/projects.html')

def resume(request):
    file = open('personal/templates/personal/documents/CV_Updated.pdf', 'rb')
    response = HttpResponse(file, content_type='application/pdf')
    return response