""" Add configuration storage module"""

from django.apps import AppConfig


class DealershipsAppConfig(AppConfig):
    """ Dealership - app confiration class"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dealership_app'
