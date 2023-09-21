"""
Function utilities to be used througout the application
"""
from textblob import TextBlob


def correct_spellings(sentence: str):
    """
    Utility function to correct the spelling of a sentence

    Args:
        sentence (str): the sentence to be corrected

    Returns:
        str: the corrected sentence
    """
    corrected_sentence = TextBlob(sentence).correct()
    return corrected_sentence

def validate_index(index, size):
    """
    Utility function to ensure that an index is valid

    Args:
        index (int): the index to be validated
        size (int): length of the list to validate the index on

    Returns:
        bool: returns True if the index is valid and False otherwise
    """
    if index is not None and index.isdigit():
        index = int(index)
        if 0 <= index < size:
            return True
    return False
