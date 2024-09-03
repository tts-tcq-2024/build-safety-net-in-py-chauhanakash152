SOUNDEX_DIC = {
    'b': '1', 'f': '1', 'p': '1', 'v': '1',
    'c': '2', 'g': '2', 'j': '2', 'k': '2',
    'q': '2', 's': '2', 'x': '2', 'z': '2',
    'd': '3', 't': '3', 'l': '4', 'm': '5',
    'n': '5', 'r': '6'
}


def generate_soundex_word(word):
    """
    Generate the Soundex code representation for a given word.

    This function maps each character in the word to its corresponding
    Soundex digit using the SOUNDEX_DIC dictionary. Characters not found
    in the dictionary are replaced with '0'.

    Parameters:
    word (str): The word to be encoded.

    Returns:
    str: A string of digits representing the Soundex encoding of the word.
    """
    word_soundex = ''
    for character in word:
        word_soundex += SOUNDEX_DIC.get(character.lower(), '0')
    return word_soundex

def should_include_char(char, prev_char):
    """
    Determine if a character should be included in the formatted Soundex code.

    This function checks if a character is different from the previous character
    and is not '0'.

    Parameters:
    char (str): The current character to be checked.
    prev_char (str): The previous character to compare against.

    Returns:
    bool: True if the character should be included, False otherwise.
    """
    return char != prev_char and char != '0'


def formate_soundex_word(word_soundex):
    """
    Format the Soundex code by removing consecutive duplicate digits.

    This function removes consecutive duplicate digits from the Soundex
    code, except for the first character. It also removes any '0' digits,
    which represent characters not in the SOUNDEX_DIC dictionary.

    Parameters:
    word_soundex (str): The Soundex code to be formatted.

    Returns:
    str: The formatted Soundex code without consecutive duplicates.
    """
    formatted_soundex = []
    prev_char = word_soundex[0]  # Start with the first character

    # Start from the second character since the first is retained as is
    for char in word_soundex[1:]:
        if should_include_char(char, prev_char):
            formatted_soundex.append(char)
        prev_char = char

    return ''.join(formatted_soundex)


def generate_soundex(word):
    """
    Generate the complete Soundex code for a given word.

    This function generates the full Soundex code, including retaining
    the first letter of the word, formatting the subsequent Soundex
    digits, and ensuring the code is four characters long by padding
    with zeros if necessary.

    Parameters:
    word (str): The word to be encoded into Soundex.

    Returns:
    str: The Soundex code for the word, which is a letter followed by
         three digits.
    """
    if not word:
        return ""
    word_soundex = generate_soundex_word(word)
    soundex_code = word[0].upper() + formate_soundex_word(word_soundex)
    soundex_code = soundex_code[:4].ljust(4, '0')
    return soundex_code
