"""
This module provides functions to decode Morse code into text.
"""

from morse.mapping import MORSE

# Morse -> Letter map
REVERSE_MORSE = {value: key for key, value in MORSE.items()}


def decode_word(morse_word: str) -> str:
    """
    Decodes a single Morse word into text.
    Letters are separated by spaces.
    """
    letters = morse_word.split()
    return "".join(REVERSE_MORSE[letter] for letter in letters if letter in REVERSE_MORSE)


def decode(morse_text: str) -> str:
    """
    Decodes the given Morse code into text.
    Words are separated by a pipe (|) and letters by a space.
    """
    words = morse_text.split("|")
    decoded_words = [decode_word(word.strip()) for word in words]
    return " ".join(decoded_words)


if __name__ == "__main__":
    # Example usage for one word
    print(decode(".- -... -.-."))  # ABC

    # Example usage for one sentence
    print(decode(".... . -.-- | .--- ..- -.. ."))  # HEY JUDE
