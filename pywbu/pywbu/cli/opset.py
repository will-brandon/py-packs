"""
opset.py

Type:       Python Script
Author:     Will Brandon
Created:    July 2, 2023
Revised:    -

Defines a class that represents a set of operations to use for an argument parser positional
argument.
"""

from argparse import ArgumentParser, Namespace
from pywbu.cli.op import Operation


class OperationSet(object):
    """
    Represents a set of operations to use for an argument parser positional argument.
    """

    __name: str
    """
    The name of the positional argument.
    """

    __ops: set[Operation]
    """
    The internal set of operation objects.
    """

    def __init__(self, name: str) -> None:
        """
        Creates a new operation set object given a name for the positional argument.
        """

        # Initialize the parent class for formality.
        super().__init__()

        # Initialize the positional argument name and the empty set of operations.
        self.__name = name
        self.__ops = set()
    

    def name(self) -> str:
        """
        Returns the name of the operation set positional argument.
        """
        
        return self.__name


    def add_operation(self, op: Operation) -> None:
        """
        Adds the given operation to the set. Fails and raises an exception if an operation with the
        same name is already in the set.
        """

        # Raise an exception if an operation with the same name already exists in the set.
        if any(op.name == existing_op.name() for existing_op in self.__ops):
            raise KeyError(f'An operation with the name "{op.name}" already exists in the set.')

        # Add the operation to the set.
        self.__ops.add(op)
    

    def add_operations(self, *ops: Operation) -> None:
        """
        Adds the given list of operations to the set. Fails and raises an exception if an operation
        with the same name is already in the set.
        """

        # Go through each operation in the set and add it.
        for op in ops:
            self.add_operation(op)


    def configure_parser(self, parser: ArgumentParser, required: bool=True) -> None:
        """
        Registers the positional argument and each argument subparser of each operation the given
        parser. The parser will then recognize the operations as options for the new positional
        argument.
        """

        # Create a set of subparsers that will hold the individual operation parsers.
        subparsers = parser.add_subparsers(dest=self.__name, required=required)

        # For each registered operation configure the subparsers set to contain the appropriate
        # parser for the operation.
        for op in self.__ops:
            op.configure_subparsers(subparsers)
    
    
    def process_args(self, args: Namespace) -> None:
        """
        Searches the argument namespace to find the positional argument relevant to this operation
        set and executes the operation which was specified.
        """

        # Check each operation in the set to see if it's name is the specified operation.
        for op in self.__ops:

            # Compare the names by retrieving the argument in the namespace by attribute accessor.
            if op.name() == getattr(args, self.__name):
                
                # If a match was found, execute the operation and return from the function.
                op.exec(args)
                return
