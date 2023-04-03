import unittest
import sys
sys.path.insert(0, '/home/project/xzceb-flask_eng_fr/final_project/machinetranslation')
from translator import english_to_french,french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test_englishToFrench(self): 
        self.assertNotEqual(english_to_french(''),'') # test for null input
        self.assertEqual(english_to_french('Hello'), 'Bonjour')  # test when 3.0 is given as input the output is 9.0.

class TestFrenchToEnglish(unittest.TestCase): 
    def test_frenchToEnglish(self): 
        self.assertNotEqual(french_to_english(''),'') # test for null input
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test when -3.1 is given as input the output is -6.2.
       
unittest.main()
