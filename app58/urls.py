from django.urls import path
from . import views

urlpatterns = [
    path('app58/', views.factorial_view, name='app58'),
]
