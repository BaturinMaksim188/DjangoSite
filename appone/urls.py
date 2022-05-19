from django.urls import path, include
from appone.views import *

urlpatterns = [
	#Фальтрация по "рубрике объявления", ещё не написано
	#path('<int:rubric_id>/', by_rubric),
	
	#Страница 127.0.0.1/appone
	path('', index),
]