"""
dismantleop.py

Type:       Python Script
Author:     Will Brandon
Created:    July 2, 2023
Revised:    -

Defines a dismantle operation class which represents the command-line dismantle operation.
"""

import os
from pathlib import Path
from argparse import ArgumentParser, Namespace
import pywbu.console as csl
import stax.project as proj
from stax.cli.op import Operation


class DismantleOperation(Operation):


    def __init__(self) -> None:
        super().__init__('dismantle')
    

    def _configure_args(self, subparser: ArgumentParser) -> None:

        subparser.add_argument('path', nargs='?', default=os.getcwd())


    def exec(self, parsed_args: Namespace) -> None:

        try:

            proj.dismantle(Path(parsed_args.path))
        
        except Exception as exc:

            csl.err_exc(exc)