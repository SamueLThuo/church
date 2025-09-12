""""
WSGI config for backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information, see:
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Always point to the same settings file
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

application = get_wsgi_application()
