import unittest

from example_class import BazelPythonExample

class BazelPythonExampleTestFirst(unittest.TestCase):
    def test_addedXyears(self):
        initial_age = 15
        added_age = 32
        bpe = BazelPythonExample("John", initial_age)
        bpe.print_age()
        bpe.add_X_years(added_age)
        self.assertEqual(bpe.age, initial_age+added_age)
        bpe.print_age()


if __name__ == '__main__':
    unittest.main()