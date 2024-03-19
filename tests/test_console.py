import unittest
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


if __name__ == "__main__":
    unittest.main()
