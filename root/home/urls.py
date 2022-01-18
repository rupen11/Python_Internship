from django.urls import path, include
from .views import home

app_name = 'home'

urlpatterns = [
    path('', home, name='home')
]