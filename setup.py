# encoding: utf-8
""" Setup script. """
from distutils.core import setup

with open("bookkeeper/__init__.py") as f:
    bookkeeper = {
        k.split(' = ')[0]: k.split(' = ')[1].replace('"','').replace("\n","")
        for k in f.readlines()
        if " = " in k
    }

setup(
    name=bookkeeper['__app__'],
    version=bookkeeper['__version__'],
    author=bookkeeper['__author__'],
    author_email='hkupty@gmail.com',
    description='GNU Stow with steroids',
    long_description=""" Bookkeeper works as a symbolic link manager.
    With some more flexibility, Bookkeeper makes the management of dotfiles easy
    and painless.""",
    scripts=['bin/bk'],
    license=bookkeeper['__license__'],
    download_url='http://github.com/hkupty/bookkeeper',
    packages=['bookkeeper'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.4',
        'Topic :: System :: Filesystems',
        'Topic :: Utilities'
    ]
)
