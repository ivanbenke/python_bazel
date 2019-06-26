import unittest

from example_class import BazelPythonExample

class BazelPythonExampleTest(unittest.TestCase):
    def test_addedXyears(self):
        bpe = BazelPythonExample(1, 15)
        print "is it not so"
        self.assertEqual(bpe.add_X_years(32), 47)
    
    def test_isResultFloat(self):
        bpe = BazelPythonExample(1, 22)
        print "the result is not float"
        self.assertIsInstance(bpe.age, float)
    
    def test_isResultInt(self):
        bpe = BazelPythonExample(1, 22)
        print "the result is int"
        self.assertIsInstance(bpe.age, int)