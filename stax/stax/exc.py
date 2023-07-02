"""
exc.py

Type:       Python Script
Author:     Will Brandon
Created:    July 1, 2023
Revised:    -

Contains stax-specific exception classes.
"""


class StaxException(Exception):
    """
    The base exception for the stax package in which all other stax exceptions extend.
    """
    
    pass


class ProjectAlreadyExistsException(StaxException):
    """
    Indicates that a stax project already exists at a given location deeming an attempted action
    invalid.
    """
    
    pass


class ProjectDoesNotExistException(StaxException):
    """
    Indicates that a stax project does not exist at a given location deeming an attempted action
    invalid.
    """
    
    pass


class MalformedProjectMetadataException(StaxException):
    """
    Indicates that a stax project metadata directory is not a directory or contains malformed
    (invalid) content.
    """
    
    pass
