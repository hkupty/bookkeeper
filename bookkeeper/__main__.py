# encoding: utf-8
""" Module frontend. """
import argparse
import sys
from bookkeeper import cli

main_parser = argparse.ArgumentParser(prog='bk')

default_parser = argparse.ArgumentParser(add_help=False)
default_parser.add_argument('--verbose', '-v', action='store_true')

sourced_parser = argparse.ArgumentParser(add_help=False)
sourced_parser.add_argument('source', action='store')

subparsers = main_parser.add_subparsers(
    title='Avaliable actions',
    description='Actions for bookkeeper.',
)

init_parser = subparsers.add_parser(
    'init', help=cli.init.__doc__, parents=[default_parser]
)
init_parser.set_defaults(func=cli.init)

sync_parser = subparsers.add_parser(
    'sync', help=cli.sync.__doc__,
    parents=[default_parser]
)
sync_parser.add_argument('app', default=None, nargs='?')
sync_parser.set_defaults(func=cli.sync)

link_parser = subparsers.add_parser(
    'link', help=cli.link.__doc__, aliases=['lk'],
    parents=[default_parser, sourced_parser]
)
link_parser.add_argument('target', default='$HOME', nargs='?')
link_parser.set_defaults(func=cli.link)

list_parser = subparsers.add_parser(
    'list', help=cli.list_apps.__doc__, aliases=['ls'],
    parents=[default_parser]
)
list_parser.set_defaults(func=cli.list_apps)

unlink_parser = subparsers.add_parser(
    'unlink', help=cli.unlink.__doc__, aliases=['un'],
    parents=[default_parser, sourced_parser]
)
unlink_parser.set_defaults(func=cli.unlink)

drop_parser = subparsers.add_parser(
    'drop', help=cli.drop.__doc__, parents=[default_parser]
)
drop_parser.set_defaults(func=cli.drop)

args = main_parser.parse_args(sys.argv[1:])

if hasattr(args, 'func'):
    args.func(args)
else:
    main_parser.print_help()
