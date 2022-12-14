from pathlib import Path

from cigem.model.module import Module
from cigem.model.setup import Setup


class Package:
    """
    A container class for a package
    """

    def __init__(self, name: str, path: Path, modules: list[Module]):
        """
        Parameters
        name: the name of the package
        path: the path to the package
        modules: the modules bundled by the package
        """

        self.name = name
        self.path = path.resolve()
        self.modules = modules

    @classmethod
    def make_package(cls, path: Path):
        """
        Makes a package

        Parameters
        path: the path to the package
        """

        package_name = Setup.make_setup(path).package_name

        package_modules = [
            Module.make_module(fes)
            for fes in path.joinpath(package_name).iterdir()
            if fes.is_dir() and fes.joinpath("__init__.pyi").exists()
        ]

        return cls(package_name, path, package_modules)
