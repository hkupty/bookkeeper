# encoding: utf-8
""" Core functionality.

This is where we understand and implement
the logic behind the whole process.
"""
import os
from bookkeeper.util import get_path
from bookkeeper.persist import DB


def link(source, target):
    """ Install all items in app as symlinks in target. """
    _db = DB.get_instance()
    full_source = os.path.abspath(source)
    _, app = os.path.split(full_source)
    target_path = get_path(target)
    _db.add_app(app, full_source, target_path)


def list_apps():
    """ Show all installed packages. """
    _db = DB.get_instance()
    print("Installed Apps")
    print("{0:<15}{1:<35}{2:<35}".format("APP", "PATH", "INSTALLED AT"))
    for app, source, target in _db.fetch_app():
        print("{0:<15}{1:<35}{2:<35}".format(
            app, source, target
        ))
    print("Not Installed Apps (local folder)")
    print("{0:<15}{1:<35}".format("APP", "PATH"))
    for i in os.listdir(os.curdir):
        if os.path.isdir(i):
            print("{0:<15}{1:<35}".format(
                i, os.path.abspath(i)
            ))


def sync(app=None):
    """ Sync all items from source.

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
        sync_folder(app, source_path, target_path)


def sync_file(file_path, target_path):
    """ Sync files.

    :param file_path:
    :param target_path:
    """
    if os.path.exists(target_path) and not os.path.islink(target_path):
        raise os.error("File exists.")
    elif os.path.islink(target_path):
        pass
    else:
        os.symlink(file_path, target_path)


def sync_folder(app, folder_path, target_path):
    """ Sync folders.

    :param folder_path: source folder.
    :param target_path: target folder.
    """
    if os.path.exists(target_path):
        if DB.get_app_for_folder(target_path) == app:
            return
        if not os.path.isdir(target_path):
            raise os.error("Target folder is a file.")
        elif not os.path.islink(target_path):
            for item in os.listdir(folder_path):
                full_item_path = os.path.join(folder_path, item)
                new_target_path = os.path.join(target_path, item)
                if os.path.isdir(full_item_path):
                    sync_folder(app, full_item_path, new_target_path)
                else:
                    sync_file(full_item_path, new_target_path)
        else:
            _db = DB.get_instance()
            if _db.count_target_path(target_path) > 1:
                os.remove(target_path)
                os.mkdir(target_path)
            sync_folder(folder_path, target_path)
    else:
        os.symlink(folder_path, target_path)


