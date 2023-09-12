from django.shortcuts import render
from .models import Events

# Create your views here.
def home(requset):
    events = Events.objects
    return render(requset, 'events/home.html',  {'events': events})
