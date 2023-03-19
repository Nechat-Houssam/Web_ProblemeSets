import json
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse

entries = []

def home(request):
    context = {
        'entries': entries
    }

    # Check if an entry_id parameter is present in the GET parameters
    entry_id = request.GET.get('entry_id')
    if entry_id:
        context['entry_id'] = int(entry_id)

    return render(request, 'home.html', context)

def add_entry(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        name = request.POST.get('name')
        name = name.capitalize()
        entry_id = len(entries) + 1
        entries.append({'id': entry_id, 'name': name, 'content': content})
        # Redirect to the homepage with an entry_id parameter
        return HttpResponseRedirect('/my_app/?entry_id={}'.format(entry_id))
    return render(request, 'add_entry.html')

def entry(request, entry_id):
    # Find the entry with the specified id
    for entry in entries:
        if entry['id'] == entry_id:
            # Return the entry as JSON
            return JsonResponse(entry)
    # If the entry was not found, return a 404 error
    return JsonResponse({'error': 'Entry not found.'}, status=404)
