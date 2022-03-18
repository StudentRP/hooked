from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "main_body/home.html", {'title': 'Home'})


def equipment(request):
    return render(request, 'main_body/equipment.html', {'title': 'Equipment'})


def techniques(request):
    return render(request, 'main_body/techniques.html', {'title': 'Techniques'})


def features(request):
    return render(request, 'main_body/features.html', {'title': 'Features'})

