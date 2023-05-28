from django.urls import path
from .views import *

urlpatterns = [
    path('home', home, name='home'),
    path('chat', chat, name='chat'),
    path('about', about, name='about'),
    path('chatAPI', chatAPI, name='chatAPI'),
    

]