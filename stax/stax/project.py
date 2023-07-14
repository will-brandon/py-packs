"""
init.py

Type:       Python Script
Author:     Will Brandon
Created:    June 30, 2023
Revised:    July 14, 2023

Manages stax projects.
"""

from pathlib import Path
from uuid import uuid1
from datetime import date
import shutil as shu
import pywbu.filesystem as fs
from stax.config import Config, create_config


PROJ_META_DIR_NAME = '.stax'
"""
The name of the directory that indicates that the parent directory contains a stax project. Stax
metadata is stored within the directory.
"""

PROJ_CONFIG_FILE_NAME = 'config.json'
"""
The name of the configuration file.
"""


class Project(object):

    root: Path
    """
    The canonical path to the root directory of the project.
    """

    meta_dir: Path
    """
    The canonical path to the metadata directory in the project.
    """

    def __init__(self, root: Path) -> None:

        # Ensure the root directory is a stax project.
        if not is_project(root):
            raise FileNotFoundError(f'No stax project exists at "{root}".')

        # Initialize the root directory and metadata directory canonical path.
        self.root = fs.canonical_path(root)
        self.meta_dir = self.root / PROJ_META_DIR_NAME
    

    def dismantle(self) -> None:
        """
        Deinitializes (dismantle) the stax project. This simply removes the metadata directory.
        After the project has been dismantled do not attempt to use more functionality on the
        object as it will result in undefined behavior.
        """

        # If the metadata directory does not exist within the given directory raise an exception becayse
        # the directory is not a stax project.
        if not self.meta_dir.is_dir():
            raise FileNotFoundError(f'Failed to dismantle stax project at "{self.root}" because ' \
                                    + 'the directory is not a stax project.')

        # Remove the metadata directory.
        shu.rmtree(self.meta_dir)


    def config(self, path: Path=fs.cwd()) -> Config:
        """
        Returns the configuration manager for the project's configuration file.
        """

        # Create a path to the configuration file within the project metadata directory.
        path = self.meta_dir / PROJ_CONFIG_FILE_NAME

        # Return a configuration object for a configuration file at the given path. The object
        # constructor will raise an exception if the file doesn't exist.
        return Config(path)


def create_project(root: Path, name: str=None, author: str=None, desc: str=None) -> None:
    """
    Creates a stax project in the given directory. If the directory does not already exist it is
    recursively created. This also creates a metadata directory within the project.
    """

    # Ensure the root path is canonical.
    root = fs.canonical_path(root)

    # Create a path to the metadata directory within the project directory.
    meta_dir = root / PROJ_META_DIR_NAME

    # If the intended path for the metadata directory points to a file instead raise an exception.
    if meta_dir.is_file():
        raise NotADirectoryError(f'Failed to create stax project at "{root}" because the ' \
                              + f'"{PROJ_META_DIR_NAME}" item already exists and is a file ' \
                              + 'instead of a directory.')
    
    # If the metadata directory already exists raise an exception because a stax project must
    # already exist in the given directory.
    if meta_dir.is_dir():
        raise FileExistsError(f'Failed to create stax project at "{root}" because the directory ' \
                              + 'is already a stax project.')
    
    # Ensure the name is not empty (None is file because a default value will be assigned).
    if name == '':
        raise ValueError('Failed to create stax project with a blank name.')
    
    # If the project name string is None use the root directory name as the project name.
    name = root.name if not name else name

    # Recursively create the metadata directory at the given path (inherently creating the project
    # directory also if it does not already exist.) Assign the proper permissions.
    meta_dir.mkdir(511, True, True)

    # Create a new universal unique identifier for the project.
    uuid = uuid1()

    # Create a path to the configuration file within the project metadata directory.
    config_path = meta_dir / PROJ_CONFIG_FILE_NAME

    # Initialize the configuration file with todays date as the project creation date.
    config = create_config(config_path, uuid, name, date.today(), author, desc)

    config.set_module('hello', date.today(), 'test module')


def is_project(root: Path) -> bool:
    """
    Determines whether the given path points to a directory that is the root of a stax project.
    """

    # Create a path to the metadata directory within the project directory.
    meta_dir = root / PROJ_META_DIR_NAME

    # If the project contains a metadata subdirectory, assume it is a project.
    return meta_dir.is_dir()


def enclosing_project(path: Path=fs.cwd()) -> Project:
    """
    Finds the project enclosing the given path. If an enclosing project does not exist None is
    returned. If there are nested projects the bottommost project in the tree is found. By default
    the current working directory is used to determine the enclosing project in the working session.
    """

    # Use the canonical equivalent of the path.
    path = fs.canonical_path(path)
    
    # If the path is a project return a project object. This is recursive base case #1.
    if is_project(path):
        return Project(path)
    
    # If the path is the root return None as no project could be found (both compared paths are
    # already anonical). This is recursive base case #2.
    if path == fs.ROOT:
        return None

    # Recursively check the parent directory to see if it is a stax project.
    return enclosing_project(path.parent)
