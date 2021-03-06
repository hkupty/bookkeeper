# encoding: utf-8
"""Core functionality.

This is where we understand and implement
the logic behind the whole process.
"""
import os
from bookkeeper.util import get_path
from bookkeeper.persist import DB
from bookkeeper.sync import sync as sync_items


def link(source, target):
    """Install all items in app as symlinks in target."""
    _db = DB.get_instance()
    full_source = os.path.abspath(source)
    _, app = os.path.split(full_source)
    target_path = get_path(target)
    _db.add_app(app, full_source, target_path)


def list_apps():
    """Show all installed packages."""
    _db = DB.get_instance()
    print("Installed Apps")
    print("{0:<15}{1:<35}{2:<35}".format("APP", "PATH", "INSTALLED AT"))
    for app, source, target in _db.fetch_app():
        print("{0:<15}{1:<35}{2:<35}".format(
            app, source, target
        ))
    print("Not Installed Apps (local folder)")
    print("{0:<15}{1:<35}".format("APP", "PATH"))
    # TODO: Exclude already installed apps
    for i in os.listdir(os.curdir):
        if os.path.isdir(i):
            print("{0:<15}{1:<35}".format(
                i, os.path.abspath(i)
            ))


def sync(app=None):
    """Sync all items from source.

    If file and not in target, create symlink.
    If file and in target, ignore.
    If folder and not in target, create symlink.
    If folder and symlink in target not from self,
        remove symlink, create folder and sync folder items.
    if folder and folder in target, sync folder items.
    """
    _db = DB.get_instance()
    app_l = _db.fetch_app(app)
    for app, source_path, target_path in app_l:
        for item in os.listdir(source_path):
            sync_items(
                os.path.join(source_path, item),
                os.path.join(target_path, item)
            )
