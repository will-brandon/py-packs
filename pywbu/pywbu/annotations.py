"""
annotations.py

Type:       Python Script
Author:     Will Brandon
Created:    July 2, 2023
Revised:    -

Defines functionless decorators that serve as annotations useful to marking code.
"""

from typing import Callable


def override(func: Callable) -> Callable:
    """
    Indicates that a given member function overrides a method from the parent class. The overriden
    function does not need to be abstract but it could be.
    """
    
    return func
