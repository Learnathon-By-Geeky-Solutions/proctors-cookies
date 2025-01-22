#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """
    Manage Django administrative tasks for the eProctoring application.
    
    This function sets up the Django environment and executes management commands
    passed via the command line. It handles potential import errors related to
    Django installation or virtual environment configuration.
    
    Raises:
        ImportError: If Django cannot be imported, indicating potential installation
        or configuration issues with the Django framework or Python environment.
    
    Example:
        $ python manage.py runserver
        $ python manage.py migrate
        $ python manage.py createsuperuser
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eProctoring.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
