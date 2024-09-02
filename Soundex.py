def get_soundex_code(char):
    """Returns the Soundex code for a single character."""
    mapping = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    return mapping.get(char.upper(), '0')

# def remove_irrelevant_chars(name):
#     """Removes vowels and irrelevant characters from the name except the first letter."""
#     return name[0].upper() + ''.join(
#         [char for char in name[1:] if char.upper() not in "AEIOUYHW"]
#     )

def encode_name(name):
    """Encodes the name into Soundex digits, collapsing adjacent same digits and handling separation by vowels."""
    first_letter = name[0].upper()
    encoded_digits = []
    previous_code = get_soundex_code(first_letter)
    
    for char in name[1:]:
        code = get_soundex_code(char)
        if code != '0' and (code != previous_code):
            encoded_digits.append(code)
        if len(encoded_digits) == 3:
            break

    return first_letter + ''.join(encoded_digits).ljust(3, '0')

def generate_soundex(name):
    """Generates the Soundex code for a given name."""
    if not name:
        return ""
    
    # cleaned_name = remove_irrelevant_chars(name)
    return encode_name(name)

# Test cases
print(generate_soundex("Robert"))  # Output should be "R163"
print(generate_soundex("Rupert"))  # Output should be "R163"
print(generate_soundex("Rubin"))   # Output should be "R150"
print(generate_soundex("Ashcraft")) # Output should be "A261"
print(generate_soundex("Ashcroft")) # Output should be "A261"
print(generate_soundex("Tymczak"))  # Output should be "T522"
print(generate_soundex("Pfister"))  # Output should be "P236"
print(generate_soundex("Honeyman"))  # Output should be "H555"
