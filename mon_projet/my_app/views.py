from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


entries = []

def home(request):
    
    context = {
        'entries': entries
    }

    
    return render(request, 'home.html', context)


def add_entry(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        name = request.POST.get('name')
        name = name.capitalize()
        entries.append({'name': name, 'content': content})

    return render(request, 'add_entry.html')