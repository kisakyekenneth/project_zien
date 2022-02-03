from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def say_hello(request):
    # Here we can pull data from db, send email
    return render(request, 'index.html', {'name': 'Kenneth'})
