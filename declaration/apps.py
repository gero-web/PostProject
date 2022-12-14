from django.apps import AppConfig
from django.db.models.signals import post_save
class DeclarationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'declaration'

    def ready(self) -> None:
        import  declaration.signal
        
      
        