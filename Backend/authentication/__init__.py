from django.apps import AppConfig

class AuthenticationAppConfig(AppConfig):
    name = 'backend.apps.authentication'
    label = 'authentication'
    verbose_name = 'Authentication'

    def ready(self):
        import register.apps.authentication.signals

default_app_config = 'backend.apps.authentication.AuthenticationAppConfig'