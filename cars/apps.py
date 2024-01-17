from django.apps import AppConfig


class CarsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cars'

    def ready(self):
        # carrega os signas do arquivo cars.signals ao rodar a aplicação
        import cars.signals # noqa
