from django.shortcuts import render
from django.views import View
from .models import News as Mb_News
from .models import Announcements as Mb_Announcements
from django.contrib.auth.decorators import login_required


# def home(request):
#     return render(request, "main_body/home.html", {'title': 'Home'})


class Home(View): # class based view seems to be working
    def get(self, request):
        return render(request, "main_body/home.html", {'title': 'Home'})


class News(View): # class based view seems to be working
    def get(self, request):
        return render(request, "main_body/news.html", {'title': 'News', 'news': Mb_News.objects.all()})


class Announcements(View): # class based view seems to be working
    def get(self, request):
        return render(request, "main_body/announcements.html", {'title': 'Announcements', 'announcements': Mb_Announcements.objects.all()})


def equipment(request):
    return render(request, 'main_body/equipment.html', {'title': 'Equipment'})


@login_required
def techniques(request):
    return render(request, 'main_body/techniques.html', {'title': 'Techniques'})


def features(request):
    return render(request, 'main_body/features.html', {'title': 'Features'})
