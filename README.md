# Wizard Talk

Scripts for talking like a wizard.

* Generate rune-encoded messages to send to your friends!

* Generate random wizard comments for simulating a chat room full of wizards, mages, and witches.



### Usage

`python talk.py`

`encode_rune("message")`
`decode_rune("<rune msg>")`




### Rune Information

No direct mapping, so no guarantee to get the same latin letter back, but it is pretty close.

Example c, translated to rune, then back to english becomes q
See comments in the rune map for characters that may have issues.

https://en.wikipedia.org/wiki/Elder_Futhark


```
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
```



### learning for scraping social media

Shout out to https://apify.com 
I would not have been able to do the instagram comment scraping without it.
