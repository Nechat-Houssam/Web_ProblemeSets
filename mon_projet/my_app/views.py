from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):

    text = """<h1>Bienvenue sur mon blog !</h1>
              <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>"""
    
    return HttpResponse(text)


def add_entry(request):

    text2 = """ <!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Add Entry</title>
  </head>
  <body>
    <h1>Add Entry</h1>
    <form action="{% url 'add_entry' %}" method="post">
     
      <label for="name">Name:</label>
      <input type="text" name="name" maxlength="20" required>
      <br>
      <label for="content">Content:</label>
      <textarea name="content" rows="4" cols="50" maxlength="120" required></textarea>
      <br>
      <input type="submit" value="Submit">
    </form>
    <a href="http://localhost:8000/my_app/">Back to Homepage</a>
  </body>
</html>"""

    return HttpResponse(text2)