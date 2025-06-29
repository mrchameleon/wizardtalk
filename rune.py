# Basic Elder Futhark Runic mapping (A-Z)
LATIN_TO_RUNIC = {
    'a': 'ᚨ',  # Ansuz
    'b': 'ᛒ',  # Berkano
    'c': 'ᚲ',  # Kaunan
    'd': 'ᛞ',  # Dagaz
    'e': 'ᛖ',  # Ehwaz
    'f': 'ᚠ',  # Fehu
    'g': 'ᚷ',  # Gebo
    'h': 'ᚺ',  # Hagalaz
    'i': 'ᛁ',  # Isa
    'j': 'ᛃ',  # Jera
    'k': 'ᚲ',  # Kaunan (same as C)
    'l': 'ᛚ',  # Laguz
    'm': 'ᛗ',  # Mannaz
    'n': 'ᚾ',  # Naudiz
    'o': 'ᛟ',  # Othala
    'p': 'ᛈ',  # Perthro
    'q': 'ᚲ',  # Approximate with Kaunan
    'r': 'ᚱ',  # Raido
    's': 'ᛊ',  # Sowilo
    't': 'ᛏ',  # Tiwaz
    'u': 'ᚢ',  # Uruz
    'v': 'ᚠ',  # Approximate with Fehu
    'w': 'ᚹ',  # Wunjo
    'x': 'ᛉ',  # Algiz
    'y': 'ᚤ',  # Yr
    'z': 'ᛉ',  # Approximate with Algiz
    ' ': ' ',  # Preserve spaces
}

RUNIC_TO_LATIN = {v: k for k, v in LATIN_TO_RUNIC.items()}

def decode_rune(text):
    result = []
    for char in text:
        latin = RUNIC_TO_LATIN.get(char, '?')  # '?' for unknown characters
        result.append(latin)
    return ''.join(result)


def encode_rune(text):
    runes = []
    for char in text.lower():
        rune = LATIN_TO_RUNIC.get(char, '?')  # Use '?' for unsupported chars
        runes.append(rune)
    return ''.join(runes)
