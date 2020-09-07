"""Exception classes for all of spaTab."""


class SpaTabException(Exception):
    """Plain spaTab exception."""


class BadChooseException(SpaTabException):
    """Except raised when user write bad command."""
