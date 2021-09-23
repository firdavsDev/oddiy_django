from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
# Create your views here.
class HomePageView(ListView):
    model=Post
    template_name='home.html'

class YangliklarView(ListView):
    model=Post
    template_name='yanglik.html'

class OnlineQabulView(ListView):
    model=Post
    template_name='qabul.html'

class BizHaqimizdaView(ListView):
    model=Post
    template_name='haqimizda.html'  