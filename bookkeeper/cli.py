# encoding: utf-8
""" Command Line Interface.

Every set of params and input shall and will be treated here.
"""
from __future__ import absolute_import


def init(fargs):
    """ Init the db. """
    from bookkeeper.persist import install, DB
    DB.set_verbose(fargs.verbose)
    install()


def sync(fargs):
    """ Sync all installed links. """
    target_app = fargs.target



def link(fargs):
    """ Link target with destination. """
    pass


def unlink(fargs):
    """ Unlink target. """
    pass


def drop(fargs):
    """ Drop the database. """
    pass
