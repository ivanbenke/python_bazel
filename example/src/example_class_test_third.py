import unittest

from example_class import BazelPythonExample

class BazelPythonExampleTestThird(unittest.TestCase):    
    def test_isResultInt(self):
        bpe = BazelPythonExample("Fido", 2.2)
        self.assertIsInstance(bpe.age, int)
        bpe.print_age()


if __name__ == '__main__':
    unittest.main()