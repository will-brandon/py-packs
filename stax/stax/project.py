"""
init.py

Type:       Python Script
Author:     Will Brandon
Created:    June 30, 2023
Revised:    July 5, 2023

Manages stax projects.
"""

from pathlib import Path
from uuid import uuid1
from datetime import date
import shutil as shu
import pywbu.filesystem as fs
import stax.config as cfg


META_DIR_NAME = '.stax'
"""
The name of the directory that indicates that the parent directory contains a stax project. Stax
metadata is stored within the directory.
"""

CONFIG_FILE_NAME = 'config.json'
"""
The name of the configuration file.
"""


def is_project(root: Path) -> bool:
    """
    Determines whether the given path points to a directory that is the root of a stax project.
    """

    # Create a path to the metadata directory within the project directory.
    meta_dir_path = root / META_DIR_NAME

    # If the project contains a metadata subdirectory, assume it is a project.
    return meta_dir_path.is_dir()


def root(path: Path=fs.cwd()) -> Path:
    """
    Finds the path to the root of the stax project encompasing the given path. If no enclosing
    project exists None is returned. If there are nested projects the bottommost project in the tree
    is found.
    """

    # Use the canonical equivalent of the path.
    path = fs.canonical_path(path)
    
    # If the path is a project return the path. This is recursive base case #1.
    if is_project(path):
        return path
    
    # If the path is the root return None as no project could be found (both compared paths are
    # already anonical). This is recursive base case #2.
    if path == fs.ROOT:
        return None

    # Recursively check the parent directory to see if it is a stax project.
    return root(path.parent)


def config(path: Path=fs.cwd()) -> cfg.Config:
    """
    Returns a configuration manager object for a configuration file within the stax project
    encompasing the given path.
    """

    # Ensure the root directory is a stax project.
    if not is_project(root):
        raise FileNotFoundError(f'Failed to get the configuration for stax project at "{root}"' \
                                + 'because the directory is not a stax project.')

    # Create a path to the configuration file within the project metadata directory.
    path = root / META_DIR_NAME / CONFIG_FILE_NAME

    # Return a configuration object for a configuration file at the given path.
    return cfg.Config(path)


def init(root: Path, name: str=None, author: str=None, desc: str=None) -> None:
    """
    Initializes a stax project in the given directory. If the directory does not already exist it
    is recursively created. This also creates a metadata directory within the project.
    """

    # Create a path to the metadata directory within the project directory.
    meta_dir_path = root / META_DIR_NAME

    # If the intended path for the metadata directory points to a file instead raise an exception.
    if meta_dir_path.is_file():
        raise NotADirectoryError(f'Failed to create stax project at "{root}" because the ' \
                              + f'"{META_DIR_NAME}" item already exists and is a file instead of ' \
                              + 'a directory.')
    
    # If the metadata directory already exists raise an exception because a stax project must
    # already exist in the given directory.
    if meta_dir_path.is_dir():
        raise FileExistsError(f'Failed to create stax project at "{root}" because the directory ' \
                              + 'already a stax project.')
    
    # Ensure the name is not empty (None is file because a default value will be assigned).
    if name == '':
        raise ValueError('Failed to create stax project with a blank name.')
    
    # If the project name string is None use the root directory name as the project name.
    name = root.name if not name else name

    # Recursively create the metadata directory at the given path (inherently creating the project
    # directory also if it does not already exist.) Assign the proper permissions.
    meta_dir_path.mkdir(511, True, True)

    # Create a new universal unique identifier for the project.
    uuid = uuid1()

    # Create a path to the configuration file within the project metadata directory.
    config_path = root / META_DIR_NAME / CONFIG_FILE_NAME

    # Initialize the configuration file with todays date as the project creation date.
    config = cfg.init(config_path, uuid, name, date.today(), author, desc)

    config.set_module('hello', date.today(), 'test module')
    

def dismantle(root: Path) -> None:
    """
    Deinitializes (dismantle) a stax project in the given directory. This simply removes the
    metadata directory.
    """

    # Create a path to the metadata directory within the project directory.
    meta_dir_path = root / META_DIR_NAME

    # If the metadata directory does not exist within the given directory raise an exception becayse
    # the directory is not a stax project.
    if not meta_dir_path.is_dir():
        raise FileNotFoundError(f'Failed to dismantle stax project at "{root}" because the ' \
                                + 'directory is not a stax project.')

    # Remove the metadata directory.
    shu.rmtree(meta_dir_path)
