"""
Function utilities to be used througout the application
"""

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

class OpenAIServiceError(Exception):
    """
    Custom exception for OpenAI service errors.
    """

    def __init__(self, message):
        super().__init__(message)
