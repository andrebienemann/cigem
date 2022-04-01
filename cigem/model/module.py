from pathlib import Path

from cigem.model.function import Function


class Module:
    """
    A container class for a module
    """

    def __init__(self, name: str, path: Path, functions: list[Function]):
        """
        Parameters
        name: the name of the module
        path: the path to the module
        functions: the functions bundled by the module
        """

        self.name = name
        self.path = path.resolve()
        self.functions = functions

    @classmethod
    def make_module(cls, path: Path):
        """
        Mekes a module

        Parameters
        path: the path to the module
        """

        name = path.parts[1]

        stub_content = path.joinpath("__init__.pyi").read_text()
        functions = Function.make_functions(stub_content)

        return cls(name, path, functions)
