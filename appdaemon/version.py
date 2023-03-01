# Conditional import to support Python 3.7
try:
    from importlib.metadata import version, PackageNotFoundError
except ImportError:  # for Python<3.8
    from importlib_metadata import version, PackageNotFoundError

# Retrieve package version using metadata from the package itself
# https://pypi.org/project/setuptools-scm/
try:
    __version__ = version("appdaemon")
except PackageNotFoundError:
    # package is not installed
    pass
