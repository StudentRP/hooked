from django.shortcuts import render
from django.views import View

# Create your views here.


# def home(request):
#     return render(request, "main_body/home.html", {'title': 'Home'})


class Home(View): # class based view seems to be working
    def get(self, request):
        return render(request, "main_body/home.html", {'title': 'Home'})


def equipment(request):
    return render(request, 'main_body/equipment.html', {'title': 'Equipment'})


def techniques(request):
    return render(request, 'main_body/techniques.html', {'title': 'Techniques'})


def features(request):
    return render(request, 'main_body/features.html', {'title': 'Features'})
