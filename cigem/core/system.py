from os import system
from pathlib import Path


def call_build(path: Path):
    setup = path.joinpath("setup.py")
    system(f"python3 {setup} build")


def call_install(path: Path):
    setup = path.joinpath("setup.py")
    system(f"python3 {setup} install")
