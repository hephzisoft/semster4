from django.shortcuts import render

def regsiter (request):
    return render(request, 'users/register.html')
