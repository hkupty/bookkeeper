# encoding: utf-8
"""Some commonly used functions and stuff."""
import os


def get_path(path):
    """Return expanded path.

    :param path: Possibly contracted path.
    :return: Expanded path.
    """
    return (
        os.path.expandvars(path)
        if '$' in path else
        os.path.expanduser(path)
    )
