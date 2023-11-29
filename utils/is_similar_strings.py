def is_similar_strings(string_1, string_2, threshold=.6):
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