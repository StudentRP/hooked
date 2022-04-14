from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
from django.urls import reverse_lazy
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


class CreateNews(CreateView):
    """dj view that save the creation of a form"""
    model = Mb_News # which db relates to
    fields = ['title', 'content'] # fields of interest
    # success_url = '/news/' # replacement for models get_absolute_url meth! (3 ways to do redirect, this, reverse_lazy & models get_absolute_url)
    success_url = reverse_lazy('mb-news') # url back ref name

    def form_valid(self, form):
        """Defaulting the author to the current user . Must override form_valid from parent to assign author (docs pg 317)"""
        form.instance.author = self.request.user # sets the current logged in user as the author
        return super().form_valid(form) # recalls the validate method


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




# def create_news(request):
#     if request.method == 'POST':
#         form = NewsCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('mb-news')
#
#     else:
#         form = NewsCreationForm()
#     return render(request, 'main_body/news_form.html', {'form': form})
















