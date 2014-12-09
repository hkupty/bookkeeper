# encoding: utf-8
""" Core functionality.

This is where we understand and implement
the logic behind the whole process.
"""
import os
from bokkeeper.persist import DB


def sync(app, target="$HOME", exclude=None):
    """ Install all items in app as symlinks in target. """
    _db = DB.get_instance()
    exclude = exclude or []

    for item in os.listdir(app):
        is_file = os.path.isfile(item)

        os.symlink(
            os.path.join(app, item),
            os.path.join(target, item)
            target_is_directory=(not is_file)
        )

        _db.add_item(app, item, "file" if is_file else "folder")

