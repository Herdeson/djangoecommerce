import os

DEBUG =True

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.dirname(BASE_DIR, 'db.sqlite3'),
    }
}
