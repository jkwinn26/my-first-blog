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

# Replace below wih the following and save when you get the "populate isn't reentrant" error
# Then put everything back to how it was! -jkw (see http://stackoverflow.com/questions/27093746/django-stops-working-with-runtimeerror-populate-isnt-reentrant)
#def application(environ, start_response):
#    if environ['mod_wsgi.process_group'] != '': 
#        import signal
#        os.kill(os.getpid(), signal.SIGINT)
#    return ["killed"]

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

#import iit.monitor
#iit.monitor.start(interval=1.0)
