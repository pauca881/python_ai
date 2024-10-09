#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()

# Create environment in anaconda
#conda create --name ecommerce
# Open terminal of that terminal
#pip install django
# django-admin.exe startproject project
# Go to settings an add the new app in INSTALLED_APPS
#Install SQLLite Viewer in my VSCode
#Important! Before create python .\manage.py startapp saludo, I have to add in the settings.py