def test_version_is_defined():
    from appdaemon.version import __version__

    assert __version__ is not None
