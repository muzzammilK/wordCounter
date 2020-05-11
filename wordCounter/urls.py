
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('counts/', views.count, name='count'),
    path('about/', views.info, name='info'),
]
