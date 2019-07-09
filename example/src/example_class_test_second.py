import unittest

from example_class import BazelPythonExample

class BazelPythonExampleTestSecond(unittest.TestCase):
    def test_isResultName(self):
        bpe = BazelPythonExample("Martin", 11)
        self.assertIsInstance(bpe.name, str)
        bpe.print_name()


if __name__ == '__main__':
    unittest.main()