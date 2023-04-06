import unittest
from translator import english_to_french as e2f, french_to_english as f2e

class test_e2f(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(e2f('Hello'), 'Bonjour') 
        self.assertNotEqual(e2f(' '), 'Anything') 
        
class test_f2e(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(f2e('Bonjour'), 'Hello') 
        self.assertNotEqual(f2e(' '), 'Quelque Chose')
        
unittest.main()