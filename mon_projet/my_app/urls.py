from django.urls import path
from . import views

app_name = 'my_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_entry, name='add_entry'),
    path('entry/<int:entry_id>/', views.entry, name='entry'),
]