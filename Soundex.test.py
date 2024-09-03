import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):

    def test_generate_soundex(self):
        self.assertEqual(generate_soundex(""), "")
        self.assertEqual(generate_soundex("PFISTER"), "P236")
        self.assertEqual(generate_soundex("TYMCZAK"), "T522")
        self.assertEqual(generate_soundex("HONEYMAN"), "H555")
        self.assertEqual(generate_soundex("Rubin"), "R150")
        self.assertEqual(generate_soundex("Ashcraft"), "A226")
    
if __name__ == '__main__':
    unittest.main()
