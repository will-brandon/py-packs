"""
init.py

Type:       Python Script
Author:     Will Brandon
Created:    June 30, 2023
Revised:    -

Manages stax projects.
"""

from pathlib import Path
import shutil as shu
from stax.exc import *


META_DIR_NAME = '.stax'
"""
The name of the directory that indicates that the parent directory contains a stax project. Stax
metadata is stored within the directory.
"""


def init(path: Path) -> None:
    """
    Initializes a stax project in the given directory. If the directory does not already exist it
    is recursively created. This also creates a metadata directory within the project.
    """

    # Create a path to the metadata directory within the project directory.
    meta_dir_path = path / META_DIR_NAME

    # If the intended path for the metadata directory points to a file instead raise an exception.
    if meta_dir_path.is_file():
        raise MalformedProjectMetadataException(f'Failed to create stax project at "{path}" ' \
                                                + f'because the "{META_DIR_NAME}" item is a file ' \
                                                + 'instead of a directory.')

    # If the metadata directory already exists raise an exception because a stax project must
    # already exist in the given directory.
    if meta_dir_path.is_dir():
        raise ProjectAlreadyExistsException(f'Failed to create stax project at "{path}" because ' \
                                            + 'the directory is already a stax project.')

    # Recursively create the metadata directory at the given path (inherently creating the project
    # directory also if it does not already exist.)
    meta_dir_path.mkdir(511, True, True)

    

def dismantle(path: str) -> None:
    """
    Deinitializes (dismantle) a stax project in the given directory. This simply removes the
    metadata directory.
    """

    # Create a path to the metadata directory within the project directory.
    meta_dir_path = path / META_DIR_NAME

    # If the metadata directory does not exist within the given directory raise an exception becayse
    # the directory is not a stax project.
    if not meta_dir_path.is_dir():
        raise ProjectDoesNotExistException(f'Failed to dismantle stax project at "{path}" because' \
                                           + ' the directory is not a stax project.')

    # Remove the metadata directory.
    shu.rmtree(meta_dir_path)
