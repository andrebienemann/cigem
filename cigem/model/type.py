class Type:
    def __init__(self, ctype: str, fstring: str):
        self.ctype = ctype
        self.fstring = fstring

    @classmethod
    def make_type(cls, string: str):
        type = string.strip()

        if type == "int":
            return cls("int", "i")

        if type == "float":
            return cls("float", "f")

        if type == "str":
            return cls("char*", "s")

        return cls("PyObject", "O")
