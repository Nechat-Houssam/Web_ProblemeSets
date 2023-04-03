import json
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from .models import Quote, Person

def home(request):
    quotes = Quote.objects.all()
    context = {
        'quotes': quotes
    }
    return render(request, 'home.html', context)

def add_entry(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        person_id = request.POST.get('person')
        person = Person.objects.get(pk=person_id)
        quote = Quote(content=content, person=person)
        quote.save()
        # redirection

        return HttpResponseRedirect('/my_app/')
    # Retrieve all persons to populate the dropdown list
    persons = Person.objects.all()
    context = {
        'persons': persons
    }
    return render(request, 'add_entry.html', context)

def entry(request, entry_id):
    try:
        quote = Quote.objects.get(pk=entry_id)
        data = {
            'id': quote.pk,
            'name': quote.person.name,
            'content': quote.content
        }
        return JsonResponse(data)
    except Quote.DoesNotExist:
        return JsonResponse({'error': 'enté non trouvée'}, status=404)
