from django.shortcuts import render
from django.http import HttpResponse
# from django .models import Orders

def Orders(request):
    return render(request, 'orders/index.html')

