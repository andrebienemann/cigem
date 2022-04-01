class Type:
    """
    A container class for a type
    """

    def __init__(self, ctype: str, fstring: str):
        """
        Parameters
        ctype: the c type of the function return type
        fstring: the formatting string of the function return type
        """

        self.ctype = ctype
        self.fstring = fstring

    @classmethod
    def make_type(cls, string: str):
        """
        Mekes a type

        Paramters
        string: a string containing the function return type
        """

        type = string.strip()

        if type == "int":
            return cls("int", "i")

        if type == "float":
            return cls("float", "f")

        if type == "str":
            return cls("char*", "s")

        return cls("PyObject", "O")
