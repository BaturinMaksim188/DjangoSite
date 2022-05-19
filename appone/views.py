from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import *

#Функция вывода на сайт данных из базы данных в шаблоне index.html
def index(request):
	bbs = Bb.objects.all()
	return render(request, 'appone/index.html', {'bbs': bbs})

#Функция вывода приветствия на главном экране
def mainP(request):
    return HttpResponse("<h1>Главная страница практического приложения <br>(по учебнику Django)</h1>")