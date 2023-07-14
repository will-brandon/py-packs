"""
config.py

Type:       Python Script
Author:     Will Brandon
Created:    July 6, 2023
Revised:    July 14, 2023

Provides a class that produces objects to manage a stax project configuration file.
"""

from pathlib import Path
from uuid import UUID
from datetime import date
import json
import stax.project as proj


DATE_FORMAT = '%Y-%m-%d'
"""
The format used to store dates in the configuration file.
"""

JSON_INDENT = 2
"""
The level of indent to use for formatting JSON. A value of None will not format the JSON at all. A
value of 0 will insert newlines but no indentation.
"""


class Config:

    path: Path
    """
    The path to the configuration file.
    """


    def __init__(self, path: Path) -> None:
        """
        Creates a configuration data object for a file with the given path.
        """

        # If the configuration file doesn't exist raise an exception.
        if not path.is_file():
            raise FileNotFoundError(f'Failed to get the configuration data from the configuration' \
                                    + f'file at "{path}" becuase it does not exist.')
        
        # Initialize the path property.
        self.path = path


    def __model_template(
            self,
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


    def __module_template(self, name: str, creation_date: date, desc: str=None) -> dict:
        """
        Returns a dictionary object representing a module a configuration model. A module name, creation
        date, and optional description will be placed in the model.
        """

        return {
            "name": name,
            "creation_date": date.strftime(creation_date, DATE_FORMAT),
            "description": desc
        }


    def __read(self) -> dict:
        """
        Reads the configuration file into a configuration model object.
        """

        # Open the configuration file for reading in an auto-closeable block.
        with open(self.path, 'r') as file:

            # Read the model object from the JSON in the configuration file.
            return json.load(file)


    def __write(self, model: dict) -> None:
        """
        Writes a model dictionary object to the configuration file. The file must already exist.
        """
    
        # Open the configuration file for writing in an auto-closeable block.
        with self.path.open('w') as file:

            # Write the model object as JSON into the configuration file.
            json.dump(model, file, indent=JSON_INDENT)
    

    def model(self) -> dict:
        return self.__read()

    
    def reset(self,
              uuid: UUID,
              name: str,
              creation_date: date,
              author: str=None,
              desc: str=None) -> None:

        # Create a template data model object to insert into the configuration file.
        model = self.__model_template(uuid, name, creation_date, author, desc)

        # Write the model to the configuration file at the given path.
        self.__write(model)
    

    def set_module(self, name: str, creation_date: str, desc: str=None) -> bool:
        """
        Sets the given module data in the configuration file. If a model with the given name already
        exists the properties of that module are updated and true is returned.
        """

        # Create a model for a module.
        module_model = self.__module_template(name, creation_date, desc)

        # Read the current model.
        model = self.__read()

        # Check to see if a module with the given name already exists and keep track of its index
        # within the modules list in the model.
        for i, module in enumerate(model['modules']):
        
            # If a module with the given name already exists, modify the entry.
            if module['name'] == name:
                
                # Set the module model at the given index to the new updated model.
                model['modules'][i] = module_model

                # Write the model to the configuration file and return true indicating that the
                # module already exists and was updated.
                self.__write(model)
                return True

        # Create the new module model in the new updated model.
        model['modules'].append(module_model)

        # Write the model to the configuration file and return false indicating that the module did
        # not already exist and was created.
        self.__write(model)
        return False


def init(
        path: Path,
        uuid: UUID,
        name: str,
        creation_date: date,
        author: str=None,
        desc: str=None) -> Config:
    """
    Creates a new configuration file at the given path. The given project UUID, name, creation date,
    optional author, and optional description will be placed in the JSON model. A configuration
    manager object is returned.
    """

    # If the configuration file already exists raise an exception.
    if path.is_file():
        raise FileExistsError(f'Failed to create configuration file at "{path}" because the file ' \
                              + 'already exists.')
    
    # Create the configuration file with the proper permissions.
    path.touch(438, False)

    config = Config(path)
    config.reset(uuid, name, creation_date, author, desc)

    return config
