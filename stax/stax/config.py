"""
config.py

Type:       Python Script
Author:     Will Brandon
Created:    July 6, 2023
Revised:    -

Manages stax project configurations.
"""

from pathlib import Path
from uuid import UUID
from datetime import date
import json
import stax.project as proj


CONFIG_FILE_NAME = 'config.json'
"""
The name of the configuration file.
"""

DATE_FORMAT = '%Y-%m-%d'
"""
The format used to store dates in the configuration file.
"""

JSON_INDENT = 2
"""
The level of indent to use for formatting JSON. A value of None will not format the JSON at all. A
value of 0 will insert newlines but no indentation.
"""


def model_template(uuid: UUID, proj_name: str, proj_author: str, proj_creation_date: date) -> dict:
    """
    Returns a dictionary object representing the start of a configuration model. A project UUID,
    name, author, and creation date will be placed in the model.
    """

    return {
        "uuid": str(uuid),
        "name": proj_name,
        "author": proj_author,
        "creation_date": date.strftime(proj_creation_date, DATE_FORMAT),
        "modules": []
    }


def init(
        path: Path,
        uuid: UUID,
        proj_name: str,
        proj_author: str,
        proj_creation_date: date) -> None:
    """
    Creates a new configuration file at the given path. The given project UUID, name, author, and
    creation date will be placed in the JSON model.
    """

    # If the configuration file already exists raise an exception.
    if path.is_file():
        raise FileExistsError(f'Failed to create configuration file at "{path}" because the file ' \
                              + 'already exists.')
    
    # Create the configuration file with the proper permissions.
    path.touch(438, False)

    # Create a template data model object to insert into the configuration file.
    model = model_template(uuid, proj_name, proj_author, proj_creation_date)

    # Open the configuration file for writing in an auto-closeable block.
    with path.open('w') as file:

        # Write the model object as JSON into the configuration file.
        json.dump(model, file, indent=JSON_INDENT)


def init_in_proj(
        root: Path,
        uuid: UUID,
        proj_name: str,
        proj_author: str,
        proj_creation_date: date) -> None:
    """
    Creates a new configuration file in the metadata directory of a project. The given project UUID,
    name, author, and creation date will be placed in the JSON model.
    """

    # Create a path to the configuration file within the project metadata directory.
    path = root / proj.META_DIR_NAME / CONFIG_FILE_NAME

    # Delegate to the path-explicit initializer.
    init(path, uuid, proj_name, proj_author, proj_creation_date)


def read(path: Path) -> dict:
    """
    Reads the configuration file at the given path into a configuration model object.
    """

    # If the configuration file does not exist raise an exception.
    if not path.is_file():
        raise FileNotFoundError(f'Failed to read nonexistent configuration file: "{path}".')

    # Open the configuration file for reading in an auto-closeable block.
    with open(path, 'r') as file:

        # Read the model object from the JSON in the configuration file.
        return json.load(file)


def read_in_proj(root: Path) -> dict:
    """
    Reads the configuration file for a project with the given root path into a configuration model
    object.
    """
    
    # Create a path to the configuration file within the project metadata directory.
    path = root / proj.META_DIR_NAME / CONFIG_FILE_NAME

    # Delegate to the path-explicit reader.
    return read(path)


def add_module(path: Path, uuid: UUID, name: str, creation_date: str) -> bool:

    model = read(path)

    # Change this so it looks for the name and uuid properties within each model object
    #if uuid in model['modules'] or name in model['modules']:
   #     return False

    model['modules']
    return True


def add_module_in_proj(root: Path) -> bool:
    
    # Create a path to the configuration file within the project metadata directory.
    path = root / proj.META_DIR_NAME / CONFIG_FILE_NAME

    # Delegate to the path-explicit add module function.
    return add_module(path)
