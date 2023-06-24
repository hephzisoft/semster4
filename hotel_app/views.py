from django.shortcuts import render

def home (request):
    return render (request, 'hotel_app/home.html')
