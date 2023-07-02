"""
op.py

Type:       Python Script
Author:     Will Brandon
Created:    July 2, 2023
Revised:    -

Defines an abstract class that represents a command-line argument operation specified as a
positional argument.
"""

from abc import ABC, abstractmethod
from argparse import ArgumentParser, Namespace, _SubParsersAction


class Operation(ABC):
    """
    Represents an abstract command-line argument operation specified as a positional argument.
    """

    __name: str
    """
    The name of the positional argument option.
    """

    __help: str
    """
    A brief help message about the operation.
    """

    __desc: str
    """
    A long description of the operation.
    """


    def __init__(self, name: str, help: str=None, desc: str=None) -> None:        
        """
        Creates a new operation object and supplies the name of the operation option as well as a
        brief help message and long description. The class is abstract so this constructor should
        only be called in the constructor of subclasses.
        """

        # Initialize the parent class for formality.
        super().__init__()

        # Initialize the name, help, and description strings.
        self.__name = name
        self.__help = help
        self.__desc = desc
    
    
    def name(self) -> str:
        """
        Returns the name of the operation set positional argument option.
        """
        
        return self.__name
    
    
    def configure_subparsers(self, subparsers: _SubParsersAction) -> None:
        """
        Registers the positional argument option with the subparsers object. A new subparser is
        created for the option and its arguments are configured.
        """
        
        # Create a subparser for the operation option.
        subparser = subparsers.add_parser(self.__name, help=self.__help, description=self.__desc)

        # Configure the arguments of the subparser.
        self._configure_args(subparser)
    
    
    @abstractmethod
    def _configure_args(self, subparser: ArgumentParser) -> None:
        """
        Configures the arguments of the subparser.
        """

        pass
    

    @abstractmethod
    def exec(self, args: Namespace) -> None:
        """
        Executes the operation given a namespace of parsed arguments.
        """

        pass
