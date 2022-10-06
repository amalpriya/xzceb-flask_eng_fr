import unittest

from translator import english_to_french,french_to_english

class TestEnglish(unittest.TestCase):
    def testEnglish(self):
        self.assertNotEqual(english_to_french(0),0)
        self.assertEqual(english_to_french("Hello"),"Bonjour")

class TestFrench(unittest.TestCase):
    def testFrench(self):
        self.assertNotEqual(french_to_english(0),0)
        self.assertEqual(french_to_english("Bonjour"),"Hello")

unittest.main()
