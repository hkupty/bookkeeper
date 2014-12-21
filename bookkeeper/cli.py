# encoding: utf-8
""" Command Line Interface.

Every set of params and input shall and will be treated here.
"""
from __future__ import absolute_import
import sys


def init(fargs):
    """ Init the db. """
    from bookkeeper.persist import install, DB
    DB.set_verbose(fargs.verbose)
    install()

    sys.exit(0)


def sync(fargs):
    """ Sync all installed links. """
    from bookkeeper.core import sync as core_sync
    app = fargs.app
    core_sync(app)

    sys.exit(0)


def link(fargs):
    """ Link target with destination. """
    from bookkeeper.core import link as core_link
    source_path = fargs.source
    target_path = fargs.target
    core_link(source_path, target_path)

    sys.exit(0)


def list_apps(fargs):
    """ Unlink target. """
    from bookkeeper.core import list_apps as core_list
    core_list()

    sys.exit(0)


def unlink(fargs):
    """ Unlink target. """
    pass


def drop(fargs):
    """ Drop the database. """
    pass
