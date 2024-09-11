import unittest
from Soundex import generate_soundex


class TestSoundex(unittest.TestCase):

    def test_empty_word(self):
        """Test the case where the input word is empty."""
        input_word = ""
        expected_soundex = ""
        self.assertEqual(generate_soundex(input_word), expected_soundex)

    def test_single_character_word(self):
        """Test the case where the input word is a single character."""
        input_word = "A"
        expected_soundex = "A000"
        self.assertEqual(generate_soundex(input_word), expected_soundex)

    def test_word_with_no_mapped_characters(self):
        """Test the case where the input word contains characters
        not in SOUNDEX_DIC."""
        input_word = "Aeio"
        expected_soundex = "A000"
        self.assertEqual(generate_soundex(input_word), expected_soundex)

    def test_word_with_consecutive_duplicates(self):
        """Test the case where the input word has consecutive
        characters that map to the same digit."""
        input_word = "PAAT"
        expected_soundex = "P300"
        self.assertEqual(generate_soundex(input_word), expected_soundex)

    def test_word_with_all_mapped_characters(self):
        """Test the case where the input word has all characters
        mapped to digits in SOUNDEX_DIC."""
        input_word = "ACM"
        expected_soundex = "A250"
        self.assertEqual(generate_soundex(input_word), expected_soundex)

    def test_word_with_padding_needed(self):
        """Test the case where the formatted Soundex code needs
        padding to ensure it is 4 characters long."""
        input_word = "Akash"
        expected_soundex = "A220"
        self.assertEqual(generate_soundex(input_word), expected_soundex)

    def test_word_with_exactly_four_characters(self):
        """Test the case where the formatted Soundex code is
        exactly 4 characters long."""
        input_word = "Brock"
        expected_soundex = "B620"
        self.assertEqual(generate_soundex(input_word), expected_soundex)


if __name__ == "__main__":
    unittest.main()
