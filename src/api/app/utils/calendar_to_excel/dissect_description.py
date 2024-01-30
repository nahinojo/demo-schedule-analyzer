from app.utils import (
    is_similar_strings,
    remove_html
)
from app.models import (
    Demo,
    DemoEvent,
)

def dissect_description(description: str):
    """
    Dissects description string into demos and additional information.

    Parameters
    ----------
    description: str
        The description to dissect.

    Returns
    -------
    list
        The list of demos and additional information.
    """
    description = description.strip()
    has_html = "<" in description
    demo_indices = []
    demos = []
    additional_info = None
    if has_html:
        idx_demo_start, idx_demo_end = 0, 0
        for i, char in enumerate(description):
            if not idx_demo_start:
                if char == ">":
                    next_five_characters = description[i + 1 : i + 6]
                    is_demo_start = True
                    if next_five_characters in "Additional Information:":
                        break
                    for c5 in next_five_characters:
                        if c5 in {"<", ">", "/"}:
                            is_demo_start = False
                            break
                    if is_demo_start:
                        for c5 in next_five_characters:
                            if c5.isdigit() or c5.isupper():
                                idx_demo_start = i + 1
            elif not idx_demo_end:
                if char == "<":
                    prev_five_characters = description[i - 6 : i - 1]
                    is_demo_end = True
                    for c5 in prev_five_characters:
                        if c5 in {"<", ">", "/"}:
                            is_demo_end = False
                    if is_demo_end:
                        idx_demo_end = i
            else:
                demo_indices.append((idx_demo_start, idx_demo_end))
                idx_demo_start, idx_demo_end = 0, 0
        for indices in demo_indices:
            demos.append(description[indices[0] : indices[1]])
            idx_additional_info_start = demo_indices[len(demo_indices) - 1][1]
            idx_additional_info_end = len(description) - 1
            additional_info = description[
                idx_additional_info_start:idx_additional_info_end
            ]
            additional_info = remove_html(additional_info)
            additional_info = additional_info.strip()
            info_start = additional_info.find("ation") + 5
            if additional_info.find("ation:") != -1:
                info_start += 1
            additional_info = additional_info[info_start:]
            if len(additional_info) < 5 or "&nbsp;" == additional_info.strip():
                additional_info = None
    else:
        description_lines = description.splitlines()
        has_demos = False
        for i, line in enumerate(description_lines):
            if i > 0:
                line_is_addtional_info = is_similar_strings(
                    line, "Additional Information:"
                )
                if len(line) > 5 and not line_is_addtional_info:
                    has_demos = True
                elif line_is_addtional_info:
                    break
        description_lines = description_lines[1:]
        idx_description_line_additional_info_title = 0
        idx_description_line = 0
        # Scanning for 'Additional Information'
        while idx_description_line < len(description_lines):
            line = description_lines[idx_description_line]
            if len(line) <= 5:
                description_lines.pop(idx_description_line)
                idx_description_line = 0
                continue
            elif is_similar_strings(
                line[: len("Additional Informaiton:")],
                "Additional Information:",
                threshold=0.6,
            ):
                idx_description_line_additional_info_title = idx_description_line
                additional_info = description_lines[idx_description_line]
                if len(additional_info[0]) > len("Additional Information:") + 5:
                    # Case 1: Additional information is on the same line as "Additional Information" Title
                    idx_additional_info_title_end = additional_info.find(":") + 1
                    if not idx_additional_info_title_end:
                        idx_additional_info_title_end = (
                            additional_info[18:].find("on") + 2
                        )
                    additional_info = additional_info[idx_additional_info_title_end:]
                    break
                elif idx_description_line < len(description_lines) - 1:
                    # Case 2: Additional Information in the lines following "Additional Information" Title
                    idx_additional_info = idx_description_line + 1
                    additional_info_first_line = description_lines[idx_additional_info]
                    while len(additional_info_first_line) < 5:
                        if len(description_lines) - 1 > idx_additional_info:
                            idx_additional_info += 1
                            additional_info_first_line = description_lines[idx_additional_info]
                        else:
                            additional_info = None
                    if idx_additional_info == len(description_lines) - 1:
                        additional_info = additional_info_first_line
                    else:
                        additional_info_list = description_lines[idx_additional_info:]
                        additional_info = ""
                        for idx, additional_info_line in enumerate(additional_info_list):
                            additional_info_line = additional_info_line.strip(". ")
                            if not idx:
                                additional_info += additional_info_line
                            else:
                                additional_info += f". {additional_info_line}"
                    break
                elif additional_info.find("formation") != -1:
                    # Case 3: Additional Information is empty
                    additional_info = None
                    break
            idx_description_line += 1
        if has_demos:
            if idx_description_line_additional_info_title == 0:
                demos = description_lines
            else:
                demos = description_lines[:idx_description_line_additional_info_title]

    i = 0
    while i < len(demos):
        demos[i] = demos[i].strip()
        demo = demos[i]
        if len(demo) <= 5:
            demos.pop(i)
            i = 0
        elif is_similar_strings(demo, "Additional Information") or is_similar_strings(demo, "DEMONSTRATIONS:"):
            demos.pop(i)
            i = 0
        elif "&" in demo:
            idx_extra_ampersand = demo.index("&")
            demos[i] = demo[:idx_extra_ampersand]
            i = 0
        else:
            i += 1
    if additional_info is not None:
        additional_info = additional_info.replace("&nbsp;", "")
        additional_info.strip(". ")
        if additional_info[-1] not in {".", "\""}:  # .strip(".") may have failed to remove "."
            additional_info += "."
        while additional_info[0] == " ":  # .strip(" ") may have failed to remove " "
            additional_info = additional_info[1:]
    return demos, additional_info
