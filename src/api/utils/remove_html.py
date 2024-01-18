def remove_html(string):
    contains_less_than = "<" in string
    contains_greater_than = ">" in string
    if contains_less_than and contains_greater_than:
        i_start, i_end = 0, 0
        for i, char in enumerate(string):
            if char == "<":
                i_start = i
            elif char == ">":
                i_end = i + 1
                return remove_html(string[:i_start] + string[i_end:])
    elif contains_greater_than:
        i_start = string.find("<") + 1
        i_end = len(string) - 1
        return remove_html(string[i_start:i_end])
    elif contains_less_than:
        i_start = 0
        i_end = string.find(">")
        return remove_html(string[i_start:i_end])
    else:
        return string
    raise ValueError("Unable to remove HTML tags from string")
