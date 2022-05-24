from unittest import TestCase

from cigem.model.parameter import Parameter


class TestParameter(TestCase):

    def test_make_int_parameter(self):
        parameter = Parameter.make_parameter("x: int")
        self.assertEqual("x", parameter.name)
        self.assertEqual("int", parameter.ctype)
        self.assertEqual("i", parameter.fstring)
    
    def test_make_float_parameter(self):
        parameter = Parameter.make_parameter("x: float")
        self.assertEqual("x", parameter.name)
        self.assertEqual("float", parameter.ctype)
        self.assertEqual("f", parameter.fstring)

    def test_make_string_parameter(self):
        parameter = Parameter.make_parameter("x: str")
        self.assertEqual("x", parameter.name)
        self.assertEqual("char*", parameter.ctype)
        self.assertEqual("s", parameter.fstring)
