import unittest

from example_class import BazelPythonExample

class BazelPythonExampleTest(unittest.TestCase):
    def test_addedXyears(self):
        initial_age = 15
        added_age = 32
        bpe = BazelPythonExample("John", initial_age)
        bpe.print_age()
        bpe.add_X_years(added_age)
        self.assertEqual(bpe.age, initial_age+added_age)
        bpe.print_age()
    
    def test_isResultName(self):
        bpe = BazelPythonExample("Martin", 11)
        self.assertIsInstance(bpe.name, str)
        bpe.print_name()
    
    def test_isResultInt(self):
        bpe = BazelPythonExample("Fido", 22)
        self.assertIsInstance(bpe.age, int)
        bpe.print_age()

if __name__ == '__main__':
    unittest.main()