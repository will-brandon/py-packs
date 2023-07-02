"""
op.py

Type:       Python Script
Author:     Will Brandon
Created:    July 2, 2023
Revised:    -

Defines an operation class which represents a command-line argument operation.
"""

from abc import ABC, abstractmethod
from argparse import ArgumentParser, Namespace, _SubParsersAction


class Operation(ABC):

    __name: str


    def __init__(self, name: str) -> None:        
        super().__init__()

        self.__name = name
    
    
    def name(self) -> str:
        return self.__name
    
    
    def configure_subparsers(self, subparsers: _SubParsersAction) -> None:
        
        subparser = subparsers.add_parser(self.__name)
        self._configure_args(subparser)
    
    
    @abstractmethod
    def _configure_args(self, subparser: ArgumentParser) -> None:
        pass
    

    @abstractmethod
    def exec(self, parsed_args: Namespace) -> None:
        pass
