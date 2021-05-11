from django.apps import AppConfig


class BanquetsConfig(AppConfig):
    name = 'banquet'
    verbose_name = 'Банкет'
    verbose_name_plural = 'Банкеты'

    def ready(self):
        import banquet.signals



