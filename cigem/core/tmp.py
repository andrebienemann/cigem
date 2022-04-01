from functools import lru_cache
from os import system
from pathlib import Path


def create_tmp(path: Path):
    """
    Creates a tmp directory in the root of the package

    Parameters
    path: the path to the root of the package
    """

    if not tmp_exists(path):
        system(f"mkdir -p {path}/tmp")


def remove_tmp(path: Path):
    """
    Removes the tmp directory in the root of the package

    Parameters
    path: the path to the root of the package
    """

    if tmp_exists(path):
        system(f"rm -r {path}/tmp")


def write_to_tmp(path: Path, name: str, content: str):
    """
    Writes content to a file inside of the tmp directory

    Parameters
    path: the path to the root of the package
    name: the name of the file to be created
    content: the content of the file to be created
    """

    create_tmp(path)

    with open(path.joinpath("tmp").joinpath(name), "w") as file:
        file.write(content)


@lru_cache()
def tmp_exists(path: Path):
    """
    Checks whether the tmp directory exists or not
    in the root for the package

    Parameters
    path: the path to the root of the package
    """

    return path.joinpath("tmp").is_dir()
