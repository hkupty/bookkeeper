# encoding: utf-8
""" Command Line Interface.

Every set of params and input shall and will be treated here.
"""
import argparse
import sys


def init(fargs):
    """ Init the db. """
    pass


def sync(fargs):
    """ Sync all installed links. """
    pass


def link(fargs):
    """ Link target with destination. """
    pass


def unlink(fargs):
    """ Unlink target. """
    pass


def drop(fargs):
    """ Drop the database. """

if __name__ == "__main__":
    main_parser = argparse.ArgumentParser(prog='bk')

    subparsers = main_parser.add_subparsers(
        title='Avaliable actions',
        description='Actions for bookkeeper.',
    )

    init_parser = subparsers.add_parser('init', help=init.__doc__)
    init_parser.set_defaults(func=init)

    sync_parser = subparsers.add_parser('sync', help=sync.__doc__)
    sync_parser.set_defaults(func=sync)

    link_parser = subparsers.add_parser(
        'link', help=link.__doc__, aliases=['lk']
    )
    link_parser.set_defaults(func=link)

    unlink_parser = subparsers.add_parser(
        'unlink', help=unlink.__doc__, aliases=['un']
    )
    unlink_parser.set_defaults(func=unlink)

    drop_parser = subparsers.add_parser('drop', help=drop.__doc__)
    drop_parser.set_defaults(func=drop)

    args = main_parser.parse_args(sys.argv[1:])

    if hasattr(args, 'func'):
        args.func(args)
    else:
        main_parser.print_help()
