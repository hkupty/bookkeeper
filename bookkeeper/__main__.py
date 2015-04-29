# encoding: utf-8
"""Module frontend."""
import argparse
import sys
from bookkeeper import cli

MAIN_PARSER = argparse.ArgumentParser(prog='bk')

DEFAULT_PARSER = argparse.ArgumentParser(add_help=False)
DEFAULT_PARSER.add_argument('--verbose', '-v', action='store_true')

SOURCED_PARSER = argparse.ArgumentParser(add_help=False)
SOURCED_PARSER.add_argument('source', action='store')

SUBPARSERS = MAIN_PARSER.add_subparsers(
    title='Avaliable actions',
    description='Actions for bookkeeper.',
)

INIT_PARSER = SUBPARSERS.add_parser(
    'init', help=cli.init.__doc__, parents=[DEFAULT_PARSER]
)
INIT_PARSER.set_defaults(func=cli.init)

SYNC_PARSER = SUBPARSERS.add_parser(
    'sync', help=cli.sync.__doc__,
    parents=[DEFAULT_PARSER]
)
SYNC_PARSER.add_argument('app', default=None, nargs='?')
SYNC_PARSER.set_defaults(func=cli.sync)

LINK_PARSER = SUBPARSERS.add_parser(
    'link', help=cli.link.__doc__, aliases=['lk'],
    parents=[DEFAULT_PARSER, SOURCED_PARSER]
)
LINK_PARSER.add_argument('target', default='$HOME', nargs='?')
LINK_PARSER.set_defaults(func=cli.link)

LIST_PARSER = SUBPARSERS.add_parser(
    'list', help=cli.list_apps.__doc__, aliases=['ls'],
    parents=[DEFAULT_PARSER]
)
LIST_PARSER.set_defaults(func=cli.list_apps)

UNLINK_PARSER = SUBPARSERS.add_parser(
    'unlink', help=cli.unlink.__doc__, aliases=['un'],
    parents=[DEFAULT_PARSER, SOURCED_PARSER]
)
UNLINK_PARSER.set_defaults(func=cli.unlink)

DROP_PARSER = SUBPARSERS.add_parser(
    'drop', help=cli.drop.__doc__, parents=[DEFAULT_PARSER]
)
DROP_PARSER.set_defaults(func=cli.drop)

args = MAIN_PARSER.parse_args(sys.argv[1:])

if hasattr(args, 'func'):
    args.func(args)
else:
    MAIN_PARSER.print_help()
