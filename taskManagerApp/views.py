from django.shortcuts import render
from .models import List

# Create your views here.
def home(request):
    listItems = List.objects.all
    return render(request, 'home.html', {'listItems': listItems})


def about(request):
    return render(request, 'about.html', {})