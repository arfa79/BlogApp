from django.apps import AppConfig


class BlogConfig(AppConfig):
    # Specify the default_auto_field attribute to use BigAutoField for primary keys
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
