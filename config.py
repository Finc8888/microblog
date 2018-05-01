import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """Параметры конфигурации преложения."""


    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you - will - never - guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' +\
        os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    """
    Расширение Flask-SQLAlchemy принимает местоположение базы данных приложения
    из переменной конфигурации SQLALCHEMY_DATABASE_URI.
    """
    """
    Параметр конфигурации SQLALCHEMY_TRACK_MODIFICATIONS установлен в значение
    False, чтобы отключить функцию Flask-SQLAlchemy, которая  не нужна
    """
