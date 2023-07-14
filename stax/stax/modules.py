"""
modules.py

Type:       Python Script
Author:     Will Brandon
Created:    July 6, 2023
Revised:    July 14, 2023

Manages stax project web modules.
"""

from pathlib import Path
import config as cfg


MODULES_DIR_NAME = 'modules'
"""
The name of the directory that holds the module configurations.
"""


def modules(root: Path):
    return cfg.read_in_proj(root)['modules']


def init(root: Path) -> bool:
    """
    Initializes the modules directory in the project root if it doesn't already exist. If it does
    exist, any existing subdirectories are assumed to be modules and are added to the configuration.
    Returns true if and only if the modules directory was already present and any existing module
    subdirectories were recognized.
    """
    
     # Create a path to the modules directory within the project directory.
    modules_dir_path = root / MODULES_DIR_NAME

    # If the intended path for the modules directory points to a file instead raise an exception.
    if modules_dir_path.is_file():
        raise FileExistsError(f'Failed to find modules directory at "{root}" because the ' \
                              + f'"{MODULES_DIR_NAME}" item already exists and is a file instead ' \
                              + 'of a directory.')
    
    # If the modules directory does not exist, create it with the proper permissions and return
    # false.
    if not modules_dir_path.is_dir():
        modules_dir_path.mkdir(511, False, False)
        return False
    
    for item in root.iterdir():

        if item.is_dir():
            pass

    return True
    


def create(root: Path, name: str) -> None:
    pass

