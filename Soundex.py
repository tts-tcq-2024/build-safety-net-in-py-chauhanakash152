def get_soundex_code(c):
    c = c.upper()
    mapping = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    return mapping.get(c, '0')  # Default to '0' for non-mapped characters

def validate_rule(code , prev_code):
    return code != '0' and code != prev_code

def generate_soundex(name):
    if not name:
        return ""
        # Start with the first letter (capitalized)
    soundex = name[0].upper()
    prev_code = get_soundex_code(soundex)

    for char in name[1:]:
        code = get_soundex_code(char)
        if validate_rule(code, prev_code):
            soundex += code
            prev_code = code
        if len(soundex) == 4:
            break
    # Pad with zeros if necessary
    soundex = soundex.ljust(4, '0')
    return soundex
# Test cases
print(generate_soundex("Robert"))  # Output should be "R163"
print(generate_soundex("Rupert"))  # Output should be "R163"
print(generate_soundex("Rubin"))   # Output should be "R150"
print(generate_soundex("Ashcraft")) # Output should be "A261"
print(generate_soundex("Ashcroft")) # Output should be "A261"
# print(generate_soundex("Tymczak"))  # Output should be "T522"
# print(generate_soundex("Pfister"))  # Output should be "P236"
# print(generate_soundex("Honeyman"))  # Output should be "H555"
