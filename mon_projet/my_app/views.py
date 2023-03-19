from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

# Create your views here.

entries = []

def home(request):
    context = {
        'entries': entries
    }

   
    entry_id = request.GET.get('entry_id')
    if entry_id:
        context['entry_id'] = int(entry_id)

    return render(request, 'home.html', context)



def add_entry(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        name = request.POST.get('name')
        name = name.capitalize()
        entries.append({'name': name, 'content': content})
        entry_id = len(entries) - 1
       
        return HttpResponseRedirect('/my_app/?entry_id={}'.format(entry_id))
    else:
   
        return render(request, 'add_entry.html')