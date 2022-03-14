from functools import lru_cache
from os import system
from pathlib import Path


def create_tmp(path: Path):
    if not tmp_exists(path):
        system(f"mkdir -p {path}/tmp")


def remove_tmp(path: Path):
    if tmp_exists(path):
        system(f"rm -r {path}/tmp")


def write_to_tmp(path: Path, name: str, content: str):
    create_tmp(path)

    with open(path.joinpath("tmp").joinpath(name), "w") as file:
        file.write(content)


@lru_cache()
def tmp_exists(path: Path):
    return path.joinpath("tmp").is_dir()
