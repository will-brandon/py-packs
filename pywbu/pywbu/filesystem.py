"""
filesystem.py

Type:       Python Script
Author:     Will Brandon
Created:    June 30, 2023
Revised:    July 1, 2023

Contains functionality to interact with the filesystem.
"""

import os
from pathlib import Path


ROOT = Path('/')
"""
A path to the root directory on the filesystem.
"""
    
def canonical_path(path: Path) -> Path:
    """
    Determines the equivalent canonical path to the given path.
    """

    return Path(os.path.realpath(str(path)))


def canonically_equals(path1: Path, path2: Path) -> bool:
    """
    Determines whether two paths are canonically equivalent to one another. I.e. checks if the paths
    are identical after resolving any path modifiers such as "." or ".." and following any symbolic
    links.
    """

    # Convert each path to its canonical path and compare the two.
    return canonical_path(path1) == canonical_path(path2)


def parent_step(path: Path, steps: int=1) -> Path:
    """
    Traverses back a given number of steps in the directory heirarchy. By default the function
    only traverses 1 step backward. If the root directory is ever reached the function stops
    stepping backward. The returned path will always be canonical.
    """

    # Use a canonical version of the path.
    canonical = canonical_path(path)

    # If the number of backward steps to take is less than one or if the path is the root of the
    # filesystem heirarchy then just return the given path.
    if steps < 1 or canonically_equals(canonical, ROOT):
        return canonical

    # Recursively continue traversing up the directory tree if more steps are present.
    return parent_step(canonical.parent, steps - 1)
