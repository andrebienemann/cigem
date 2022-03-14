class Parameter:
    def __init__(self, name: str, ctype: str, fstring: str):
        self.name = name
        self.ctype = ctype
        self.fstring = fstring

    @classmethod
    def make_parameter(cls, string):
        name, type = map(str.strip, string.split(":"))

        if type == "int":
            return cls(name, "int", "i")

        if type == "float":
            return cls(name, "float", "f")

        if type == "str":
            return cls(name, "char*", "s")

        return cls(name, "PyObject", "O")
