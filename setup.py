# encoding: utf-8
""" Setup script. """
from distutils.core import setup
import bookkeeper

setup(
    name=bookkeeper.__app__,
    version=bookkeeper.__version__,
    author=bookkeeper.__author__,
    author_email='hkupty@gmail.com',
    description='GNU Stow with steroids',
    long_description="""A dotfile manager with a sane interface. """,
    scripts=['bin/bk'],
    license=bookkeeper.__license__,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.4',
        'Topic :: System :: Filesystems',
        'Topic :: Utilities'
    ]
)
