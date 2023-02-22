from django.urls import path

from .views import base

urlpatterns = [
    path('home/', base, {'name': 'home'}, name='home'),
    path('home/<str:name>', base)
]
