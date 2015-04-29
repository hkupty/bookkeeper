# encoding: utf-8
""" Bookkeeper.

This project intends to bring friendlier functionality to GNU Stow,
allowing quick smarter management.

It is important to note that this project is focused on enhancing and
simplifying Stow use on dot file management, so, while the enhancements
here proposed and implemented may be useful for software installation,
this is by no means the main intent of this project.
"""
from bookkeeper import persist, cli, core


__author__ = "Henry 'Ingvij' Kupty"
__app__ = "Bookkeeper"
__version__ = "0.0.2"
__license__ = "BSD"
__all__ = [ "persist", "cli", "core" ]
