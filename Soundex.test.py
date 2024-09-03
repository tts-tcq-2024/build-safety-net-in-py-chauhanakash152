import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):

    def test_empty_word(self):
        """Test the case where the input word is empty."""
        self.assertEqual(generate_soundex(''), "")

    def test_single_character_word(self):
        """Test the case where the input word is a single character."""
        self.assertEqual(generate_soundex('A'), "A000")

    def test_word_with_no_mapped_characters(self):
        """Test the case where the input word contains characters not in SOUNDEX_DIC."""
        self.assertEqual(generate_soundex('Aeio'), "A000")

    def test_word_with_consecutive_duplicates(self):
        """Test the case where the input word has consecutive characters that map to the same digit."""
        self.assertEqual(generate_soundex('BEEF'), "B100")

    def test_word_with_all_mapped_characters(self):
        """Test the case where the input word has all characters mapped to digits in SOUNDEX_DIC."""
        self.assertEqual(generate_soundex('ACM'), "A250")

    def test_word_with_padding_needed(self):
        """Test the case where the formatted Soundex code needs padding to ensure it is 4 characters long."""
        self.assertEqual(generate_soundex('Akash'), "A220")

    def test_word_with_exactly_four_characters(self):
        """Test the case where the formatted Soundex code is exactly 4 characters long."""
        self.assertEqual(generate_soundex('Brock'), "B620")
    
if __name__ == '__main__':
    unittest.main()
