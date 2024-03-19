#!/usr/bin/python3
""" Defines console unittests """
import unittest
import pep8
from io import StringIO
from console import HBNBCommand


class TestDoCreate(unittest.TestCase):
    def setUp(self):
        self.cli = HBNBCommand()

    def test_create_no_args(self):
        with self.assertRaises(SystemExit):
            self.cli.do_create("")

    def test_create_invalid_class(self):
        with self.assertRaises(SystemExit):
            self.cli.do_create("InvalidClass")

    def test_create_valid_class_no_params(self):
        self.cli.do_create("ValidClass")
        self.assertEqual(len(self.cli.storage.all()), 1)

    def test_create_valid_class_with_paramas(self):
        self.cli.do_create('ValidClass name="Test" number=1.23')
        obj = list(self.cli.storage.all().value())[0]
        self.assertEqual(obj.name, "Test")
        self.assertEqual(obj.number, 1.23)

    def testPep8(self):
        """ Test for pep8 code style """
        code_sty = pep8.StyleGuide(quiet=True)
        pyc = code_sty.check_files(["console.py"])
        self.assertEqual(pyc.total_errors, 0, "fix pep8")


if __name__ == "__main__":
    unittest.main()
