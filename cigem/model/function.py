import re

from cigem.model.parameter import Parameter
from cigem.model.type import Type


class Function:
    """
    A container class for a function
    """

    re_function = re.compile(r"\s+(\w+)\s*\(([\w,\s:]*)\)\s*->\s*(\w+)")

    def __init__(self, name: str, parameters: list[Parameter], return_type: Type):
        """
        Parameters
        name: the name of the function
        parameters: function parameters
        return_type: function return value
        """

        self.name: str = name
        self.parameters: list[Parameter] = parameters
        self.return_type: Type = return_type

    @classmethod
    def make_functions(cls, stub_content: str):
        """
        Makes functions

        Parameters
        stub_content: the content of a stub file
        """

        functions = list()

        for match in cls.re_function.findall(stub_content):
            name = match[0]

            parameters = [
                Parameter.make_parameter(parameter)
                for parameter in match[1].split(",")
                if parameter
            ]

            return_type = Type.make_type(match[2])

            functions.append(Function(name, parameters, return_type))

        return functions
