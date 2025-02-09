from input_search import regexIP
import unittest
class TestRegEx(unittest.TestCase):
    def setUp(self):
        self.regexIP=regexIP
    def test_regex(self):
        self.assertEqual(self.regexIP('3.45.231.0'), True)
