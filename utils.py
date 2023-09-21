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

