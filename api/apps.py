from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "api"

    def ready(self):
        import api.signals
        from parser.matcher import configuration_weightage, load_dataset
        configuration_weightage()
        load_dataset()

