import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(generate_soundex(""), "")

    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")

    def test_single_character_non_mapped(self):
        self.assertEqual(generate_soundex("1"), "1000")  # Non-mapped character should default to '0'

    def test_repeated_characters(self):
        self.assertEqual(generate_soundex("Sssss"), "S000")

    def test_name_with_digits(self):
        self.assertEqual(generate_soundex("J0hn"), "J500")

    def test_name_with_special_characters(self):
        self.assertEqual(generate_soundex("John@Doe"), "J530")

    def test_name_with_various_letters(self):
        self.assertEqual(generate_soundex("Cameron"), "C550")
        self.assertEqual(generate_soundex("Smith"), "S530")
        self.assertEqual(generate_soundex("Khan"), "K530")


    
if __name__ == '__main__':
    unittest.main()
