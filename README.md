Bookkeeper
==========
[![Code Health](https://landscape.io/github/hkupty/bookkeeper/master/landscape.svg)](https://landscape.io/github/hkupty/bookkeeper/master)
[![PyPI version](https://badge.fury.io/py/Bookkeeper.svg)](http://badge.fury.io/py/Bookkeeper)
[![Build Status](https://drone.io/github.com/hkupty/bookkeeper/status.png)](https://drone.io/github.com/hkupty/bookkeeper/latest)
[![Code Climate](https://codeclimate.com/github/hkupty/bookkeeper/badges/gpa.svg)](https://codeclimate.com/github/hkupty/bookkeeper)

GNU Stow with steroids!

Bookkeeper works as a symbolic link manager with some more flexibility,
making the management of dotfiles easy and painless.

Why?
----

I thought that managing my dotfiles with `GNU Stow` was easier than handling `ln -s` myself,
but still some things were missing for me, such as knowing which packages I already installed and
recursively updating nested folders.

Bookkeeper improvements
-----------------------

### List

With 5 chars one can know which packages are already installed and which are not.
```bash
$ bk ls
PACKAGE     INSTALLED
irssi       no
tmux        no
vim         yes
zsh         yes
```

### Recursive update

Updating recursively is also very easy:
```bash
$ bk sync
Syncing package 'vim'.
Done
Syncing package 'zsh'.
Added new folder:   zsh/.zsh
Added new file:     zsh/.zshrc
Sync complete!
```

### Future
New features will be implemented in the future, but keep in mind that bookkeeper, differently than `GNU Stow`,
is designed for handling dotfiles, not packages in general.


