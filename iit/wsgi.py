# """
# WSGI config for iit project.
# 
# It exposes the WSGI callable as a module-level variable named ``application``.
# 
# For more information on this file, see
# https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
# """
# 
# import os
# 
# from django.core.wsgi import get_wsgi_application
# 
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "iit.settings")
# 
# application = get_wsgi_application()

# The above ^^^ is the original wsgy.py script created by django-admin.py. -jkw

"""
WSGI config for iit project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os, sys
sys.path.append('/home/jon/web/insideit/')
sys.path.append('/home/jon/web/insideit/lib/python3.4/site-packages/') 

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "iit.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
