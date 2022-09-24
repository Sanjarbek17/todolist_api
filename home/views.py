from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    r = []
    r = requests.get('http://127.0.0.1:8000/api/get').json()
    return render(request, 'pages/home.html', context={'data': r})