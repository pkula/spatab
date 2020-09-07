"""Command-line implementation of spaTab."""
import sys

from spatab.main import application
from spatab.exceptions import BadChooseException
from spatab.main.message import usage


def main(argv=None):
    """Execute the main bit of the application."""
    if argv is None:
        argv = sys.argv[1:]
    try:
        app = application.Application(argv)
        app.run()
    except BadChooseException:
        print(usage())
    except FileNotFoundError:
        print("Choose valuable file.")
