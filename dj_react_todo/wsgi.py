"""
WSGI config for dj_react_todo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import dotenv
import pathlib

from django.core.wsgi import get_wsgi_application

debug = True

if debug:
    CURRENT_DIR = pathlib.Path(__file__).resolve().parent
    BASE_DIR = CURRENT_DIR.parent
    ENV_FILE_PATH = BASE_DIR / ".env"

    dotenv.read_dotenv(str(ENV_FILE_PATH))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj_react_todo.settings')

application = get_wsgi_application()
app = application