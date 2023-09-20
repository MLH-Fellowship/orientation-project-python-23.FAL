from textblob import TextBlob


def correct_spellings(sentence: str):
    corrected_sentence = TextBlob(sentence).correct()
    return corrected_sentence

