"""
WSGI config for pandas_example_project_2_import_csv_in_existing_table project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pandas_example_project_2_import_csv_in_existing_table.settings')

application = get_wsgi_application()
