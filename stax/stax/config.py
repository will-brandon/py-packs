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


def model_template(
        uuid: UUID,
        name: str,
        creation_date: date,
        author: str=None,
        desc: str=None) -> dict:
    """
    Returns a dictionary object representing the start of a configuration model. A project UUID,
    name, and creation date, optional author, and optional description will be placed in the model.
    """

    return {
        "uuid": str(uuid),
        "name": name,
        "creation_date": date.strftime(creation_date, DATE_FORMAT),
        "author": author,
        "description": desc,
        "modules": []
    }


def module_template(name: str, creation_date: date, desc: str=None) -> dict:
    """
    Returns a dictionary object representing a module a configuration model. A module name, creation
    date, and optional description will be placed in the model.
    """

    return {
        "name": name,
        "creation_date": date.strftime(creation_date, DATE_FORMAT),
        "description": desc
    }


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


def write(path: Path, model: dict) -> None:
    
    if not path.is_file():
        raise FileNotFoundError(f'Failed to write configuration file at "{path}" because the file' \
                                + ' does not exist.')
    
    # Open the configuration file for writing in an auto-closeable block.
    with path.open('w') as file:

        # Write the model object as JSON into the configuration file.
        json.dump(model, file, indent=JSON_INDENT)


def init(
        path: Path,
        uuid: UUID,
        name: str,
        creation_date: date,
        author: str=None,
        desc: str=None) -> None:
    """
    Creates a new configuration file at the given path. The given project UUID, name, creation date,
    optional author, and optional description will be placed in the JSON model.
    """

    # If the configuration file already exists raise an exception.
    if path.is_file():
        raise FileExistsError(f'Failed to create configuration file at "{path}" because the file ' \
                              + 'already exists.')
    
    # Create the configuration file with the proper permissions.
    path.touch(438, False)

    # Create a template data model object to insert into the configuration file.
    model = model_template(uuid, name, creation_date, author, desc)

    # Write the model to the configuration file at the given path.
    write(path, model)


def init_in_proj(
        root: Path,
        uuid: UUID,
        name: str,
        creation_date: date,
        author: str=None,
        desc: str=None) -> None:
    """
    Creates a new configuration file in the metadata directory of a project. The given project UUID,
    name, creation date, optional author, and optional description will be placed in the JSON model.
    """

    # Create a path to the configuration file within the project metadata directory.
    path = root / proj.META_DIR_NAME / CONFIG_FILE_NAME

    # Delegate to the path-explicit initializer.
    init(path, uuid, name, creation_date, author, desc)


def set_module(path: Path, name: str, creation_date: str, desc: str=None) -> bool:
    """
    Sets the given module data in the configuration file at the given path. If a model with the
    given name already exists the properties of that module are updated and true is returned.
    """

    # Create a model for a module.
    module_model = module_template(name, creation_date, desc)

    # Read the current model.
    model = read(path)

    for i, module in enumerate(model['modules']):
        
        if module['name'] == name:

            model['modules'][i] = module_model
            return True

    model['modules'].append(module_model)

    write(path, model)

    return False    


def set_module_in_proj(root: Path, name: str, creation_date: str, desc: str=None) -> bool:
    """
    Sets the given module data in the configuration file for a project with the given root path. If
    a model with the given name already exists the properties of that module are updated and true is
    returned.
    """
    
    # Create a path to the configuration file within the project metadata directory.
    path = root / proj.META_DIR_NAME / CONFIG_FILE_NAME

    # Delegate to the path-explicit add module function.
    return set_module(path, name, creation_date, desc)
