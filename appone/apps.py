from django.apps import AppConfig

#Инициализация приложения для его регистрации в settings.py
class ApponeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appone'
