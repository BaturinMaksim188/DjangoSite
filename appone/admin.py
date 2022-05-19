from django.contrib import admin

# Register your models here.
from .models import *

#Преобразование названий полей данных на админ-сайте в модели Bb
class BbAdmin(admin.ModelAdmin):
	list_display = ('title', 'content', 'price', 'published', 'rubric')
	list_display_links = ('title', )
	search_fields = ('title', 'content', )


#Регистрация моделей и их конфигураций
admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)

