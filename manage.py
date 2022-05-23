import os
import sys

solution_is_alpha = True

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CDT.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Try "
            "running 'pip install Django'."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    if solution_is_alpha: 
        pass

    main()
