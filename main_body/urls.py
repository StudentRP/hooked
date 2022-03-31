from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='mb-home'),
    path('equipment/', views.equipment, name='mb-equipment'),
    path('techniques/', views.techniques, name='mb-techniques'),
    path('features/', views.features, name='mb-features')
]
