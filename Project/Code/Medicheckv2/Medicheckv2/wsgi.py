"""
WSGI config for Medicheckv2 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""
# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Medicheckv2.settings")

# application = get_wsgi_application()


import os
import sys
import site
from django.core.wsgi import get_wsgi_application

# Add the app’s directory to the PYTHONPATH
sys.path.append('D:\Hi\wwww\Aspire\GitHub\AspireSystems-PFB\Project\Code\Medicheckv2\Medicheckv2')
sys.path.append('D:\Hi\wwww\Aspire\GitHub\AspireSystems-PFB\Project\Code\Medicheckv2')
os.environ['DJANGO_SETTINGS_MODULE'] = 'Medicheckv2.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Medicheckv2.settings")
application = get_wsgi_application()