from django.urls import path
from . import views
# from django.contrib.auth.decorators import login_required # for cbv authentication


urlpatterns = [

    path('equipment/', views.equipment, name='mb-equipment'),
    path('techniques/', views.techniques, name='mb-techniques'),
    path('features/', views.features, name='mb-features'),
    path('news/', views.News.as_view(), name='mb-news'),
    # path('news/', login_required(views.News.as_view(), login_url='login')), # not working yet
    path('announcements/', views.Announcements.as_view(), name='mb-announcements'),
    path('', views.Home.as_view(), name='mb-home'), # needs to be last looked in as slower return factor
]
