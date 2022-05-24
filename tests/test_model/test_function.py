from unittest import TestCase

from cigem.model.function import Function

class TestFunction(TestCase):

    def test_make_function(self):
        functions = Function.make_functions("def get_int() -> int: ...")
        self.assertIsNotNone(functions)
