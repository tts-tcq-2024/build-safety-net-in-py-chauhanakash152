SOUNDEX_MAPPING = {
    "0": "aeiouyhw",
    "1": "bfpv",
    "2": "cgjkqsxz",
    "3": "dt",
    "4": "l",
    "5": "mn",
    "6": "r",
}


def get_soundex_code(character):
    """
    Retrieves the Soundex code for a given character.

    Args:
        character (str): The character to map to a Soundex code.

    Returns:
        str or None: The corresponding Soundex code if the character is found, otherwise None.
    """
    return next(
        (code for code, chars in SOUNDEX_MAPPING.items() if character.lower() in chars),
        None,
    )


def format_soundex_code(soundex_code, final_string, first_character_soundex):
    """
    Determines if the Soundex code should be included in the final string.

    Args:
        soundex_code (str): The Soundex code to evaluate.
        final_string (str): The current accumulated Soundex string.
        first_character_soundex (str): The Soundex code of the first character of the name.

    Returns:
        bool: True if the Soundex code should be included in the final string, False otherwise.
    """
    return (
        soundex_code
        and not final_string.endswith(soundex_code)
        and not (len(final_string) == 1 and soundex_code in first_character_soundex)
    )


def generate_soundex(name):
    """
    Generates the Soundex code for a given name.

    Args:
        name (str): The name to generate a Soundex code for.

    Returns:
        str: A 4-character Soundex code string. If the name is empty, returns an empty string.
    """
    if not name:
        return ""

    final_string = name[0].upper()
    first_character_soundex = get_soundex_code(name[0])
    soundex_codes = [get_soundex_code(character) for character in name[1:]]
    final_string += "".join(
        soundex_code
        for soundex_code in soundex_codes
        if format_soundex_code(soundex_code, final_string, first_character_soundex)
    )

    final_string = final_string.replace("0", "")
    return final_string.ljust(4, "0")


print(generate_soundex("PFISTER"))  # returns P236
print(generate_soundex("Akash"))  # returns A220
print(generate_soundex("Aakaash"))  # returns A220
print(generate_soundex("TYMCZAK"))  # returns T522
print(generate_soundex("HONEYMAN"))  # returns H555
print(generate_soundex("PFISTER"))  # returns P236
