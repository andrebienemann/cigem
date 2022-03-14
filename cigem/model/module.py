from pathlib import Path

from cigem.model.function import Function


class Module:
    def __init__(self, name: str, path: Path, functions: list[Function]):
        self.name = name
        self.path = path.resolve()
        self.functions = functions

    @classmethod
    def make_module(cls, path: Path):
        name = path.parts[1]

        stub_content = path.joinpath("__init__.pyi").read_text()
        functions = Function.make_functions(stub_content)

        return cls(name, path, functions)
