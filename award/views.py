from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
# Create your views here.
def index(request):
    date = dt.date.today()
    projects = Projects.get_projects()
    

    return render(request, 'index.html', {"date": date, "projects":projects})