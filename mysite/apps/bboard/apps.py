from django.apps import AppConfig


class BboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bboard'
    label: str = 'bboard'
    verbose_name: str = 'Тестовые Объявления'