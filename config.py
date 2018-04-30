import os


class Config(object):
    """Параметры конфигурации преложения."""


    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you - will - never - guess'
