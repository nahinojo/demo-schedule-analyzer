def is_similar_strings(string_1, string_2, threshold=0.6):
    """
    Checks if two strings are similar.

    Parameters
    ----------
    string_1: str
        The first string.
    string_2: str
        The second string.
    threshold: float, default=0.6
        The threshold for similarity. It's the decimal representation of the percentage of characters that must match.

    Returns
    -------
    bool
        Whether the two strings are similar.
    """
    string_1 = string_1.lower()
    string_2 = string_2.lower()
    number_characters_matching = 0
    shorter_string = string_1
    longer_string = string_2
    if len(string_1) > len(string_2):
        shorter_string = string_2
        longer_string = string_1
    for idx, char in enumerate(shorter_string):
        if char == longer_string[idx]:
            number_characters_matching += 1
    accuracy = number_characters_matching / len(longer_string)
    return accuracy >= threshold
