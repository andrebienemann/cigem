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


def call_build_ext(path: Path):
    """
    Calls the build_ext command

    Parameters
    path: the path to the root of the package
    """

    setup = path.joinpath("setup.py")
    system(f"python3 {setup} build_ext --inplace")


def call_install(path: Path):
    """
    Calls the install command

    Parameters
    path: the path to the root of the package
    """

    setup = path.joinpath("setup.py")
    system(f"python3 {setup} install")


def call_unittest(path: Path):
    """
    Calls the unittest command

    Parameters
    path: the path to the root of the package
    """

    tests = path.joinpath("tests")
    system(f"python3 -m unittest discover {tests}")


def call_mkdir(path: Path):
    """
    Calls the mkdir command

    Parameters
    path: the path to the root of the package
    """
    system(f"mkdir -p {path}")


def call_rm(path: Path):
    """
    Calls the rm command

    Parameters
    path: the path to the root of the package
    """
    system(f"rm -r {path}")


def call_touch(path: Path):
    """
    Calls the touch command

    Parameters
    path: the path to the root of the package
    """
    system(f"touch {path}")
