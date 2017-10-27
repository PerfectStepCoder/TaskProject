#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AuthorizeRestApi.settings")
    # os.environ['PATH'] += ";{0}".format(os.path.dirname(os.path.dirname(__file__)))
    #print(os.environ['PATH'])
    current_folder = os.path.abspath(os.path.dirname(__file__))
    root_folder = os.path.abspath(os.path.dirname(current_folder))
    # os.environ['PATH'] += ";{0}".format(root_folder)
    # os.environ['PYTHONPATH'] += ";{0}".format(root_folder)
    sys.path.append(root_folder)
    # print("PYTHONPATH:\n", os.environ['PYTHONPATH'])
    # print("PATH:\n", os.environ['PATH'])
    # print("sys.path:\n", "\n".join(sys.path))
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
