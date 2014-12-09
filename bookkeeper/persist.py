# encoding: utf-8
""" Small database wrapper allowing install management.

This allows bookkeeper to keep track of which is installed (and where).
"""
import sqlite


class DB(object):

    """ Manages the sqlite connection. """

    _instance = None

    @classmethod
    def get_instance(cls):
        """ Singleton instance. """
        if _instance = None:
            _instance = cls()
        return _instance

    def __init__(self):
        self.connection = sql.connect('$HOME/.bookkeeper_db')

    def exec(self, command):
        """ Wrapper for sqlite exec. """
        cursor = self.connection.cursor()
        cursor.execute(command)
        cursor.commit()


def install():
    """ Create basic db. """
    db = DB.get_instance()

    db.exec("""CREATE TABLE apps
    (app text, source_path text, target_path text)
    """)
    db.exec("""CREATE TABLE inner
    (app text, object text, type text)
    """)
