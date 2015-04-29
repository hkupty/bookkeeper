# encoding: utf-8
"""Sync source on target be it file or folder.

There are some specific rules for syncing, which are specified below:
On files,
* if none, creates symlink;
* if file or folder exists, error;
* if symlink exists, 
  * if self, pass;
  * if not self, error. 

On folders, 
* if none, creates symlink;
* if file exists, error;
* if folder exists, merge;
* if symlink exists, 
  * if self, pass;
  * if folder, 
    * from bk, create folder & merge;
    * not from bk, error;
  * if file, error.
"""
import os


def sync(item_path, target_path):
    """Switch between file and folder syning."""
    if os.path.isdir(item_path):
        sync_folder(item_path, target_path)
    else:
        sync_file(item_path, target_path)


def sync_file(file_path, target_path):
    """Sync file on target path."""
    if os.path.exists(target_path) and not os.path.islink(target_path):
        raise os.error("File exists: {}".format(file_path))
    elif os.path.islink(target_path):
        pass
    else:
        os.symlink(file_path, target_path)


def sync_folder(folder_path, target_path):
    if not os.path.exists(target_path):
        os.symlink(folder_path, target_path)
    else:
        if os.path.islink(target_path):
            # Check if from self
            pass
        elif os.path.isdir(target_path):
            merge(folder_path, target_path)
        else:
            raise os.error("File exists: {}".format(folder_path))


def merge(folder_path, target_path):
    """Link all itens on folder onto target folder."""
    for item in os.listdir(folder_path):
        sync(
            os.path.join(folder_path, item),
            os.path.join(target_path, os.path.split(folder_path)[-1])
        )
