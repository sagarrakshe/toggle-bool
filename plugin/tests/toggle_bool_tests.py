import unittest
import toggle_bool as sut


@unittest.skip("Don't forget to test!")
class ToggleBoolTests(unittest.TestCase):

    def test_example_fail(self):
        result = sut.toggle_bool_example()
        self.assertEqual("Happy Hacking", result)
