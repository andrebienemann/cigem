class Parameter:
    """
    A container class for a parameter
    """

    def __init__(self, name: str, ctype: str, fstring: str):
        """
        Parameters
        name: the name of the parameter
        ctype: the c type of the parameter
        fstring: the formatting string of the parameter
        """

        self.name = name
        self.ctype = ctype
        self.fstring = fstring

    @classmethod
    def make_parameter(cls, string):
        """
        Mekes a parameter

        Parameters
        string: a string containing the parameter name and type
        """

        name, type = map(str.strip, string.split(":"))

        if type == "int":
            return cls(name, "int", "i")

        if type == "float":
            return cls(name, "float", "f")

        if type == "str":
            return cls(name, "char*", "s")

        return cls(name, "PyObject", "O")
