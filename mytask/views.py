from django.http import HttpResponse
from django.shortcuts import render

def task(request):
    return render(request, 'index.html')


def details(request):
    first = request.GET.get('first', 'default')
    last = request.GET.get('last', 'default')
    mail = request.GET.get('email', 'default')
    gender = request.GET.get('gender', 'default')
    college = request.GET.get('college', 'default')
    contact = request.GET.get('phone', 'default')

    details = {'first': first, 'last' : last, 'mail': mail, 'gender': gender, 'college': college, 'contact': contact}
    return render(request, 'details.html', details)


