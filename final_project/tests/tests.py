import unittest

from translator import english_to_french,french_to_english

class TestEnglish(unittest.TestCase):
    def testEnglish(self):
        self.assertEqual(english_to_french(" ")," ")
        self.assertEqual(english_to_french("Hello"),"Bonjour")

class TestFrench(unittest.TestCase):
    def testFrench(self):
        self.assertEqual(french_to_english(" ")," ")
        self.assertEqual(french_to_english("Bonjour"),"Hello")

unittest.main()
