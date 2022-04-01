from os import system
from pathlib import Path


def call_build(path: Path):
    """
    Calls the build command

    Parameters
    path: the path to the root of the package
    """

    setup = path.joinpath("setup.py")
    system(f"python3 {setup} build")


def call_install(path: Path):
    """
    Calls the install command

    Parameters
    path: the path to the root of the package
    """

    setup = path.joinpath("setup.py")
    system(f"python3 {setup} install")
