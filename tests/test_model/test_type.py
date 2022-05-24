from unittest import TestCase

from cigem.model.type import Type


class TestType(TestCase):

    def test_make_int_type(self):
        type = Type.make_type("int")
        self.assertEqual("int", type.ctype)
        self.assertEqual("i", type.fstring)

    def test_make_float_type(self):
        type = Type.make_type("float")
        self.assertEqual("float", type.ctype)
        self.assertEqual("f", type.fstring)
    
    def test_make_str_type(self):
        type = Type.make_type("str")
        self.assertEqual("char*", type.ctype)
        self.assertEqual("s", type.fstring)
