import os
import sys
import threading
import time
import webbrowser

from django.core.management import execute_from_command_line


def abrir_navegador():
    time.sleep(3)
    webbrowser.open("http://127.0.0.1:8000/financeiro/")


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sistema.settings")

    threading.Thread(
        target=abrir_navegador,
        daemon=True
    ).start()

    execute_from_command_line([
        sys.argv[0],
        "runserver",
        "127.0.0.1:8000",
        "--noreload",
    ])