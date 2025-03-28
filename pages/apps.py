# The line `from django.apps import AppConfig` is importing the `AppConfig` class from the
# `django.apps` module in Django. This class is used to define configuration for Django applications,
# such as specifying the default database field type (`default_auto_field`) and the name of the
# application (`name`).
from django.apps import AppConfig


# The `PagesConfig` class in Python sets the default auto field to `django.db.models.BigAutoField` for
# the `pages` app.
class PagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pages'
