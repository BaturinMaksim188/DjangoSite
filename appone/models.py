from django.db import models


class Bb(models.Model):
	#Поля вторичной модели хранения данных об объявлениях
	title = models.CharField(max_length=50, verbose_name='Товар')
	content = models.TextField(null=True, blank=True, verbose_name='Описание')
	price = models.FloatField(null=True, blank=True, verbose_name='Цена') 
	published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
	#Внешний ключ
	rubric = models.ForeignKey('Rubric', null = True, on_delete = models.PROTECT, verbose_name = 'Рубрика')
	#Класс Meta
	class Meta:
		verbose_name_plural = 'Объявления'
		verbose_name = 'Объявление'
		ordering = ['-published']


class Rubric(models.Model):
	#Поля первичной модели фильтрации
	name = models.CharField(max_length=20, db_index=True, verbose_name='Название')
	#Функция вывода названий рубрики(Вместо админ-модели в admin.py, поскольку имеем только одно поле - name)
	def __str__(self):
		return self.name
	#Класс Meta
	class Meta:
		verbose_name_plural = ('Рубрики')
		verbose_name = ('Рубрика')
		ordering = ['name']