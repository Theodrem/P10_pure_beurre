from . import *
from selenium import webdriver

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'postgres',
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': ''
        }
}
SELENIUM_WEBDRIVERS = {
'default': {
'callable': webdriver.Chrome,
'args': (),
'kwargs': {},
},}