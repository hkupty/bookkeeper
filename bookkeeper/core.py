# encoding: utf-8
""" Core functionality.

This is where we understand and implement
the logic behind the whole process.
"""
import os
from bookkeeper.persist import DB


def link(source, target):
    """ Install all items in app as symlinks in target. """
    _db = DB.get_instance()
    full_source = os.path.abspath(source)
    source_path, app = os.path.split(full_source)
    target_path = (
        os.path.expandvars(target)
        if '$' in target else
        os.path.expanduser(target)
    )
    _db.add_app(app, source_path, target_path)
